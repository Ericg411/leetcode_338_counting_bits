import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_countBits(self):
        sol = Solution()

        # Test case 1: n = 0
        n = 0
        expected = [0]
        self.assertEqual(sol.countBits(n), expected)

        # Test case 2: n = 1
        n = 1
        expected = [0, 1]
        self.assertEqual(sol.countBits(n), expected)

        # Test case 3: n = 2
        n = 2
        expected = [0, 1, 1]
        self.assertEqual(sol.countBits(n), expected)

        # Test case 4: n = 5
        n = 5
        expected = [0, 1, 1, 2, 1, 2]
        self.assertEqual(sol.countBits(n), expected)

        # Test case 5: n = 10
        n = 10
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
        self.assertEqual(sol.countBits(n), expected)\

if __name__ == "__main__":
    unittest.main()