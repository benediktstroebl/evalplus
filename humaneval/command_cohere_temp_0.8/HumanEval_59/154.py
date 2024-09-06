```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case of n being a power of 2, which has no digits after the decimal point.
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # Convert n into a string to access its digits.
    base = str(n)
    # Iterate through each digit, starting from the last.
    for i in range(len(base) - 1, -1, -1):
        # Check if the digit is prime.
        if all(base[i] != j for j in range(2, int(base[i]) + 1, 1)):
            return int(base[i])
        # If not, divide n by the digit.
        n //= int(base[i])
    return 1
```

This solution checks if the digits of the original number are prime one at a time, returning the digit as the result if it is prime. It divides the number by that digit (and any factors less than it) until it is reduced to rubble, factoring out all non-prime factors. 

The tests provided in the original task correspond to the examples provided in the problem statement and are included in the code below. These tests are executed within the `if __name__ == "__main__"` block to ensure they are only executed when the script is run directly:
```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case of n being a power of 2, which has no digits after the decimal point.
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # Convert n into a string to access its digits.
    base = str(n)
    # Iterate through each digit, starting from the last.
    for i in range(len(base) - 1, -1, -1):
        # Check if the digit is prime.
        if all(base[i] != j for j in range(2, int(base[i]) + 1, 1)):
            return int(base[i])
        # If not, divide n by the digit.
        n //= int(base[i])
    return 1

if __name__ == "__main__":
    import unittest

    class TestSuite(unittest.TestCase):
        def test_largest_prime_factor(self):
            self.assertEqual(largest_prime_factor(13195), 29)
        def test_largest_prime_factor_2048(self):
            self.assertEqual(largest_prime_factor(2048), 2)

    unittest.main()
```