### Modular Exponentiation
### ======================

We can use the built-in `pow` function in Python, which can compute the power `a` raised to `b` modulo `c` efficiently.

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The base number.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    return pow(2, n, p)
```

### Test Cases
### ===========

We can test the function using the provided test cases:

```python
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

You can run the script and see that all test cases pass.