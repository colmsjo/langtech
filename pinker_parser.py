#!/usr/bin/python
#
# Simple recursive descent parser based on Steven Pinker's book The Language Instict.
#
# Using Google Style Guide: https://google.github.io/styleguide/pyguide.html#Naming
#
# Copyright (C) 2017 Jonas Colmsjo
#
# LICENSE: MIT

import sys, getopt

DEBUG = True

def debug(*args):
    if DEBUG:
        print "DEBUG: ", args

def expected_phrase_not_found(expected_class, tokens):
    print("Expected %s: %s" % (expected_class, tokens))
    exit()

def tail(a):
    if (len(a) > 1):
        return a[1:]
    else:
        return None

DETS = ["a", "the", "one"]
NS = ["boy", "girl", "dog", "cat", "ice_cream", "candy", "hot_dogs"]
VS = ["eats", "likes", "bites"]
PS = ["with", "in", "near"]

# X([t1,t2,...,tn]) = (("X", a1, a2), [t3,...,tn])

def parse(str):
    str = str.lower().replace(".", "")
    tokens = str.split()

    return S(tokens)

def S(tokens):
    (np, tokens) = NP(tokens)                   # Mandatory

    if np == None:
        expected_phrase_not_found("NP", tokens)

    (vp, tokens) = VP(tokens)                   # Mandatory

    if vp == None:
        expected_phrase_not_found("VP", tokens)

    debug("S", np, vp, tokens)

    return (("S", np, vp), tokens)              # tokens should be None now

def NP(tokens):
    (det,  tokens) = DET(tokens)                # Optional

    (noun, tokens) = N(tokens)                  # Mandatory

    if noun == None:
        return (None, tokens)

    pp = None
    if len(tokens) > 0:
        (pp, tokens) = PP(tokens)               # Optional

    debug("NP", det, noun, pp, tokens)

    return (("NP", det, noun, pp), tokens)

def VP(tokens):
    (verb, tokens) = V(tokens)                  # Mandatory

    if verb == None:
        return (None, tokens)

    (np, tokens) = NP(tokens)                   # Mandatory

    if np == None:
        return (None, tokens)

    pp = None
    if len(tokens) > 0:
        (pp, tokens) = PP(tokens)               # Optional

    debug("VP", verb, np, pp, tokens)

    return (("VP", verb, np, pp), tokens)

def PP(tokens):
    (p, tokens) = P(tokens)                     # Mandatory

    if p == None:
        return (None, tokens)

    (np, tokens) = NP(tokens)                   # Mandatory

    debug("PP", p, np, tokens)

    return (("PP", p, np), tokens)

# Returns None if no DETERMINER is found
def DET(tokens):
    res = None

    if tokens[0] in DETS:
        res = ("DET", tokens[0])
        tokens = tokens[1:]

    debug(res, tokens)

    return (res, tokens)

# Returns None if no NOUN is found
def N(tokens):
    res = None

    if tokens[0] in NS:
        res = ("N", tokens[0])
        tokens = tokens[1:]

    debug(res, tokens)

    return (res, tokens)

# Returns None of no VERB is found
def V(tokens):
    res = None

    if tokens[0] in VS:
        res = ("V", tokens[0])
        tokens = tokens[1:]

    debug(res, tokens)

    return (res, tokens)

# Returns None if no PREPOSITION is found
def P(tokens):
    res = None

    if tokens[0] in PS:
        res = ("P", tokens[0])
        tokens = tokens[1:]

    debug (res, tokens)

    return (res, tokens)

# Show help
def help():
    print("NS: ", NS)
    print("VS: ", VS)
    print("PS: ", PS)
    print("DETS: ", DETS)

# Main
if __name__ == "__main__":
    if sys.argv[1] == "help":
        help()
        exit()

    tree = parse(sys.argv[1])
    print(tree)
