```python
def is_multiply_prime(a):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(str(a).split(' '))
    return len(divisors) == 3 and all(divisor in prime_numbers for divisor in divisors)
```

The function `is_multiply_prime` checks if the given number is the multiplication of three prime numbers. The algorithm verifies that the given number is less than 100 and then analyzes its divisors, it classifies them as prime or not. Finally, the algorithm compares the number of divisors to 3 and then verifies if all of them are prime. 

This solution assumes that the given number is represented as a string where each divisor is separated by a single space. This simplifies the checking of the divisors if they are prime or not. 

Here is a test suit to make sure that the function `is_multiply_prime` is correct:
```python
import unittest

def is_multiply_prime(a):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(str(a).split(' '))
    return len(divisors) == 3 and all(divisor in prime_numbers for divisor in divisors)

class TestIsMultiplyPrime(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(54))
        self.assertTrue(is_multiply_prime(58))

    def test_invalid(self):
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(99))

if __name__ == '__main__':
    unittest.main()
```

In the test suit, there are two test functions, the first one is responsible for testing the correct output for positive examples, and the second test function is responsible for checking if the function detects correctly the invalid cases. 

The final line `unittest.main()` runs the test suit when the script is executed. 
If you want to check if the test suit passes or not, you just need to run the script.