```python
import unittest

def modp(n: int, p: int) -> int:
    """
    Calculate 2^n modulo p.

    Args:
    n (int): The power to which 2 is raised.
    p (int): The prime number to take the modulus with.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Use the property of modular exponentiation that (a*b) % n = ((a % n) * (b % n)) % n
    # This prevents large intermediate results and reduces risk of overflow
    result = 1
    base = 2 % p  # Reduce base to its modulus equivalent
    
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base for the next iteration
        base = (base * base) % p
        # Right shift n (divide by 2) for the next iteration
        n = n // 2
    
    return result

class TestModpFunction(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()
```

This script defines a function `modp(n, p)` that calculates `2^n modulo p` using modular exponentiation. It also includes a set of test cases to verify the function's correctness. The tests cover various edge cases, including even and odd exponents, as well as different prime numbers. The `unittest` module is used to write and run these tests.