Here's a Python script that includes the `modp` function along with some test cases:
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    :param n: the exponent
    :param p: the modulus
    :return: the result of 2^n modulo p
    """
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result with base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result

if __name__ == "__main__":
    import unittest

    class TestModpFunction(unittest.TestCase):
        def test_modp(self):
            self.assertEqual(modp(3, 5), 3)
            self.assertEqual(modp(1101, 101), 2)
            self.assertEqual(modp(0, 101), 1)
            self.assertEqual(modp(3, 11), 8)
            self.assertEqual(modp(100, 101), 1)

    unittest.main(argv=[__file__])
```

This script uses the exponentiation by squaring technique to efficiently calculate 2^n modulo p. The test cases cover a variety of scenarios, including different exponents and moduli.