```python
def fib_fib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib_fib(0) == 0
    fib_fib(1) == 0
    fib_fib(2) == 1
    fib_fib(n) == fib_fib(n-1) + fib_fib(n-2) + fib_fib(n-3).

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c


# Test cases
if __name__ == "__main__":
    import unittest

    class TestFibFib(unittest.TestCase):
        def test_base_cases(self):
            self.assertEqual(fib_fib(0), 0)
            self.assertEqual(fib_fib(1), 0)
            self.assertEqual(fib_fib(2), 1)

        def test_fib_fib_numbers(self):
            self.assertEqual(fib_fib(5), 4)
            self.assertEqual(fib_fib(8), 24)

    unittest.main(argv=[__file__])
```

This script defines a function `fib_fib` that calculates the n-th element of the FibFib number sequence. It uses a loop to efficiently compute the value, only maintaining the last three values of the sequence at any given time. The script also includes a test suite to verify the correctness of the function.