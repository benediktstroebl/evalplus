```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a/b
        a, b = b, a % b
    return abs(a)


# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5

# Test cases
import unittest

class TestGCDFunction(unittest.TestCase):

    def test_gcd_of_coprime_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_of_non_coprime_numbers(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_of_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(10, 10), 10)

    def test_gcd_of_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-5, 10), 5)

if __name__ == '__main__':
    unittest.main()
```