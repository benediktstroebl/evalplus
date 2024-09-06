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

The function `is_prime` is used to check if a number is prime. Then, the function `count_up_to` starts counting from 2 up to *n* and stores each prime number in the list `primes`. It stops when `count == n`, so that the list contains the desired amount of prime numbers. 

To further ensure that the code behaves correctly, below is a simple test suite with unittest:
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
    def test_count_up_to_with_zero(self):
        """Test case where n = 0"""
        self.assertEqual(count_up_to(0), [])

    def test_count_up_to_with_one(self):
        """Test case where n = 1"""
        self.assertEqual(count_up_to(1), [])

    def test_count_up_to_with_5(self):
        """Test case where n = 5"""
        self.assertEqual(count_up_to(5), [2, 3])

    def test_count_up_to_with_11(self):
        """Test case where n = 11"""
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])

    def test_count_up_to_with_20(self):
        """Test case where n = 20"""
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_up_to_with_non_positive(self):
        """Test case where n < 0"""
        with self.assertRaises(AssertionError):
            count_up_to(-3)

if __name__ == '__main__':
    unittest.main()
```

The test suite contains several test functions that check different edges and scenarios to ensure that the `count_up_to` function behaves as expected. Each test function checks a specific condition and asserts that the function returns the expected result. The `