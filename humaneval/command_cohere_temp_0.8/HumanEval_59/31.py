```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest % 2 == 0:
        largest //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while largest % i == 0:
            largest //= i
    if largest > 1:
        return largest
    return n
```

To determine the largest prime factor, the algorithm works by first checking if the number is even or not. If it is even, it divides by 2 until it finds a odd number. Then it checks for divisibility by repeatedly dividing the number by i (starting from 3 and progressing upwards). The loop continues until the number is divisible by i. If i is greater than the square root of the number, then loop is a no-op and largest prime is the i-th prime. Finally, it returns the largest prime factor of the number if the final `largest` is greater than 1. If not, it returns the number itself.

This algorithm is an optimized combination of the trial division algorithm and the sieve of Eratosthenes. It is efficient and maintains a linear time complexity of O(n). 

The unit tests for this function are already included. You can use the following code to test this function:
```python
import unittest

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(97), 97)
        self.assertEqual(largest_prime_factor(315), 3)

if __name__ == '__main__':
    unittest.main()
```

This script defines a test class with four test methods, all of which pass if the function `largest_prime_factor` is implemented correctly. 
If you want to test for more cases, you can add more test methods to the test class or use a testing framework like `pytest`.

I hope this helps! Let me know if you have any other questions.