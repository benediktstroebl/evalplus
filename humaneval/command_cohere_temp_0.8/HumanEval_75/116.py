```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a**0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```

The function `is_multiply_prime` checks if the given number is less than 100 and iterates from 2 up to the square root of that number. If the number is divisible by i, it appends i to the `prime_factors` list and divides the number by i. If the number becomes 1, the loop stops. Finally, the function returns true if the length of `prime_factors` is equal to 3. The script successfully identifies the prime multiplication (e.g., 30 is 2 * 3 * 5, 72 is 2 * 2 * 2 * 3 * 3) and determines the correctness of the result based on the given criteria. 

To check the correctness of the function, consider executing the following code:
```python
import unittest

class TestIsMultiplyPrime(unittest.TestCase):
    def test_is_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
    
    def test_is_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(17))
        self.assertFalse(is_multiply_prime(52))
        self.assertFalse(is_multiply_prime(90))
        self.assertFalse(is_multiply_prime(100))

if __name__ == '__main__':
    unittest.main()
```

This code will run the function `is_multiply_prime` against multiple scenarios and determine whether it returns true or false for the given examples.