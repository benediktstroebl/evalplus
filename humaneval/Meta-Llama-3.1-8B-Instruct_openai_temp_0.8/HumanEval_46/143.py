```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence 
    without using recursion.

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The n-th number in the fib4 sequence.
    """
    # Base cases for the sequence
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    # Initialize the dynamic programming array with base cases
    dp = [0, 0, 2, 0]
    # Compute the fib4 sequence up to the n-th element
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
    # Return the n-th element
    return dp[n]


# Test the function
import unittest

class TestFib4(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_larger_numbers(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
```

In this script, the function `fib4` uses dynamic programming to efficiently compute the n-th element of the fib4 sequence without using recursion. The `unittest` module is used to write and run test cases for the function.