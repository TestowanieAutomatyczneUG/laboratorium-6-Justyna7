import unittest


class Hamming:
    def distance(self, a, b):
        if len(a) == len(b):
            n = 0
            for (i, x) in enumerate(a):
                if a[i] != b[i]:
                    n = n+1
            return n
        else:
            raise ValueError(r".+")


class HammingTest(unittest.TestCase):

    @unittest.skip
    def test_empty_strands(self):
        self.assertEqual(self.temp.distance("", ""), 0)

    @unittest.skip
    def test_single_letter_identical_strands(self):
        self.assertEqual(self.temp.distance("A", "A"), 0)

    @unittest.skip
    def test_single_letter_different_strands(self):
        self.assertEqual(self.temp.distance("G", "T"), 1)

    @unittest.skip
    def test_long_identical_strands(self):
        self.assertEqual(self.temp.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    @unittest.skip
    def test_long_different_strands(self):
        self.assertEqual(self.temp.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    @unittest.skip
    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("AATG", "AAA")

    @unittest.skip
    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("ATA", "AGTG")

    @unittest.skip
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("", "G")

    @unittest.skip
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.distance("G", "")

    # Utility functions
    def setUp(self):
        self.temp = Hamming()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
