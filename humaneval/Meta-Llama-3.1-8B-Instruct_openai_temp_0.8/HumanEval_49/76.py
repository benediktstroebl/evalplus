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
    # Use Python's built-in power function with the modulo operator
    # to efficiently calculate 2^n modulo p.
    return pow(2, n, p)


# Test cases
import unittest

class TestModpFunction(unittest.TestCase):
    def test_modp_examples(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()
```

This script defines the `modp` function and includes test cases using the `unittest` module. The function uses the `pow` function with three arguments to calculate 2^n modulo p efficiently. The test cases are based on the provided examples and ensure that the function behaves correctly.