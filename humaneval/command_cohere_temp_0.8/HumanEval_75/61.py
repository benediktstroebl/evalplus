```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = []
    
    for prime in primes:
        if n % prime == 0:
            divisors.append(prime)
            
    return len(divisors) == 3
``` 

The function checks if the number can be divided by any prime numbers from the primes list, and if there are exactly three divisors, returns `True`. Else, it returns `False`. 

This approach ensures that the given number is not greater than the product of 3 primes, as the list of primes (`primes`) only includes numbers less than or equal to 100. 
The unit tests for this function would be:
```python
# Testing suite
import unittest

class TestIsMultiplyPrime(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_multiply_prime(60))
        self.assertTrue(is_multiply_prime(36))
        self.assertTrue(is_multiply_prime(72))

    def test_negative_numbers(self):
        self.assertFalse(is_multiply_prime(-40))
        self.assertFalse(is_multiply_prime(-70))
        self.assertFalse(is_multiply_prime(-10))

    def test_numbers_with_more_than_three_divisors(self):
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(35))
        self.assertFalse(is_multiply_prime(54))

if __name__ == '__main__':
    unittest.main()
``` 

This testing suite includes three tests for the function `is_multiply_prime` with different cases. 
However, you may want to add more tests, including edge cases, to further validate the function and ensure its robustness. 
If you intend to use this code, it is recommended to test it on a broader range of numbers and edge cases to ensure its correctness and stability.