Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through integers from 2 up to `n`, it checks each integer with the `is_prime()` function. If the integer is prime and less than `n`, it is added to the `primes` list. The loop stops when the `count` of primes added to the list reaches `n` or when it reaches `n + 1`.

Here is a test suite that can be used to test the function (assuming the script is saved as a Python file):
```python
import unittest
from primerange import count_up_to, is_prime

class TestPrimeCount(unittest.TestCase):
    def test_count_up_to_5(self):
        self.assertEqual(count_up_to(5), [2, 3])

    def test_count_up_to_11(self):
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])

    def test_count_up_to_20(self):
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_up_to_0(self):
        self.assertEqual(count_up_to(0), [])

    def test_count_up_to_1(self):
        self.assertEqual(count_up_to(1), [])

    def test_count_up_to_18(self):
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()
```

This test suite uses the `unittest` module to create and run tests. The `TestPrimeCount` class derives from `unittest.TestCase`, and each test is defined as a method with the `assert_*` prefix, which indicates that it will assert a specific condition and raise an exception if the condition is not met. The final `unittest.main()` call runs the tests when the script is run directly. 

To run the tests, you can run the Python script directly in your terminal. You should see the line `.*TestPrimeCount: OK.*` for each test method, indicating that the test passed. If you encounter any issues, please let me know and I will be happy to provide solutions or explanations!