Here's a self-contained Python script that defines the `modp` function:

```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
import unittest

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

The `modp` function calculates `2^n mod p` using the property of modular arithmetic that `(a*b) mod p = ((a mod p) * (b mod p)) mod p`. We start with `result = 1` and then multiply it by 2 in a loop `n` times, taking the modulus `p` after each multiplication.

The provided test cases are defined in a `unittest` framework to ensure the `modp` function works as expected. The `unittest.main()` function is called when the script is run directly to execute these test cases.