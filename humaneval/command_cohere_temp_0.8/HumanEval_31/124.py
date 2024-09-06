Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns `False`. However, if the number is not prime, it returns `True`.

Here's a snippet of code you can use to test this function:
```python
# Test the is_prime function
import unittest

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
```

This block of code uses the `unittest` module to run a series of test cases that check if the `is_prime` function returns the expected outputs.