import unittest
import pinker_parser

#
# The test results needs to be verified manually (asserts are not used)
#

class TestPinkerParser(unittest.TestCase):

    def test1(self):
        s = "The dog likes ice_cream"
        print "----- TEST1:", s
        print pinker_parser.parse(s)

    def test2(self):
        s = "The boy with a dog likes ice_cream"
        print "----- TEST2:", s
        print pinker_parser.parse(s)


if __name__ == '__main__':
    unittest.main()
