```python
import math

def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if digit in digits and is_prime(int(digit)):
            count += 1
    return count
```

The provided solution uses a simple approach to solve the problem by:
1. Defining a helper function `is_prime` to check if a given number is prime or not. 
2. The `hex_key` function basically loops through each digit in the hexadecimal number and counts the digits that correspond to prime numbers.

The `is_prime` function is used to check if the digit represented by the digit in the string is a prime number or not. The `hex_key` function counts the number of digits that are prime, and returns the count. 

This solution assumes that the input is always correct and does not perform any validation on the input to ensure it is a valid hexadecimal number.

To test this, you can run the following tests:
```python
# Testing the given solution
import unittest

class TestHexKey(unittest.TestCase):
    def test_hex_key_empty_string(self):
        self.assertEqual(hex_key(""), 0)

    def test_hex_key_single_digit_prime(self):
        self.assertEqual(hex_key("B"), 1)

    def test_hex_key_mixed_string(self):
        self.assertEqual(hex_key("0123456789ABCDEF"), 6)

    def test_hex_key_only_non_prime_digits(self):
        self.assertEqual(hex_key("20210707"), 0)

    def test_hex_key_only_prime_digits(self):
        self.assertEqual(hex_key("2B2D5"), 2)

if __name__ == '__main__':
    unittest.main()
```

This will run the tests and assert that the `hex_key` function returns the expected output for the given inputs.