```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    return pow(2, n, p)


# Test cases
import unittest

class TestModpFunction(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == "__main__":
    unittest.main(argv=[str(__file__)])
```

This script includes the `modp` function that calculates the result of 2^n modulo p using the built-in `pow` function with three arguments. It handles negative exponents by using the `pow` function's behavior when the third argument is given.

The test cases are included to ensure the function works as expected in various scenarios. The tests use the `unittest` framework to run the tests when the script is executed directly.