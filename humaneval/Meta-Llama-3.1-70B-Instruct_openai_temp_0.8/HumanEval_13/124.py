```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Using the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

# Test the function
import unittest

class TestGCDFunction(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(101, 103), 1)

if __name__ == '__main__':
    unittest.main()
```