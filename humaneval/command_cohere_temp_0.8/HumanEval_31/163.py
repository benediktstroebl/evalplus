Here's a Python script with a self-contained function `is_prime` that follows the problem statement and hopefully passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function checks if a given number is less than 2, returns False. If the number is greater than 1, it iterates from 2 to the square root of the number and checks if the number is divisible by any integer in this range. If the number is divisible by any of them, it returns False. If it isn't, it returns True.

To run the tests, you can use a script like this:
```python
import unittest
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_is_prime_true(self):
        self.assertTrue(is_prime(101))
    def test_is_prime_false(self):
        self.assertFalse(is_prime(6))
    def test_is_prime_11(self):
        self.assertTrue(is_prime(11))
    def test_is_prime_13441(self):
        self.assertTrue(is_prime(13441))
    def test_is_prime_61(self):
        self.assertTrue(is_prime(61))
    def test_is_prime_false_4(self):
        self.assertFalse(is_prime(4))
    def test_is_prime_false_1(self):
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
```

This script uses the `unittest` module to define a test class with several test methods, each testing a specific condition of the `is_prime` function. When you run this script, the `unittest` module automatically runs all the test methods and reports the results, ensuring that the function's behavior matches all the provided tests. 

Note that this approach provides relatively efficient prime checking for larger values of `n`, as it uses the technique of checking divisibility only up to the square root of `n`. 

It's important to note that the Python script provided is assuming the presence of the `unittest` module, which is included in Python's standard library. If you're using a environment or virtual environment that doesn't have `unittest` imported, you might need to add it or adjust the script accordingly.