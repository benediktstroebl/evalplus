Here's a Python script with a self-contained function that solves the prime-checking problem, along with a script to run the provided tests:
```python
# The main program and function
def is_prime(n):
    if n < 2:
        return False
    
    # Check if the number is divisible from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Script to run the tests
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

The `is_prime` function is the same as the one you provided, and the `test_is_prime` function is a collection of test cases to verify the correctness of the `is_prime` function.

To run the test, copy this code into a `.py` file and execute the file. The `unittest` framework will run the tests and report if the `is_prime` function passes or fails each of these tests.