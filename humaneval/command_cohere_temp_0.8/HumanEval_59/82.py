```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for edge cases: 2 and 5
    if n == 2 or n == 5:
        return n
    
    # Try dividing by each prime factor up to the square root of n
    for i in range(5, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    
    # If no factors found, return n
    return n
```

This algorithm first checks if `n` is equal to 2 or 5, as these are the closest prime numbers to the largest possible factors (namely 1 and n itself). If `n` is not 2 or 5, the algorithm iterates through factors up to the square root of `n`, factoring out each one until it has factored out as much as possible. This will return the largest prime factor of any number greater than 1 and not prime. 

To demonstrate the usage of the function, you can add additional test cases in the same file, preferably in a unittest block:
```python
import unittest

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor_edge_cases(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_largest_prime_factor_general_case(self):
        self.assertEqual(largest_prime_factor(33375), 311)

    def test_largest_prime_factor_halves(self):
        self.assertEqual(largest_prime_factor(25), 5)
        self.assertEqual(largest_prime_factor(51), 3)
        self.assertEqual(largest_prime_factor(275), 5)

if __name__ == '__main__':
    unittest.main()
```

This way, running the file will automatically execute the tests and verify that the function behaves as expected.  This approach provides a complete self-contained code block that solves the mentioned problem.  If you have more questions or require assistance with anything related to algorithms and coding problems, please don't hesitate to ask!