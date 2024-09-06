```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If it is a prime number, it is added to the `primes` list and the `count` variable is incremented. Once the `count` variable reaches the value of `n`, the loop is terminated and the list of prime numbers is returned.

To ensure the correctness of the `is_prime()` function and the `count_up_to()` function, it is advisable to incorporate unit tests to cover different cases like:
- Test cases for edges of the prime number spectrum
- Test cases that cover the threshold of the `n` parameter. 
- Test cases for numbers that have been excluded from the list of prime numbers. 

Here is an example of adding test cases using the `unittest` module:
```python
import unittest
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes

class TestCountUpTo(unittest.TestCase):
    def test_count_up_to_with_small_n(self):
        self.assertEqual(count_up_to(3), [2, 3])
        self.assertEqual(count_up_to(5), [2, 3, 5])
        self.assertEqual(count_up_to(7), [2, 3, 5, 7])
        self.assertEqual(count_up_to(10), [2, 3, 5, 7])

    def test_count_up_to_with_large_n(self):
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(count_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_count_up_to_with_0(self):
        self.assertEqual(count_up_to(0), [])

    def test_count_up_to_with_1