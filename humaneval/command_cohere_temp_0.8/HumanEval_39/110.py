Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Generates the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev, curr = 0, 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    
    # Start searching from the (n-1)-th Fibonacci number
    # Since we already computed the n-2-th Fibonacci number (prev), 
    # we can skip that iteration
    for i in range(prev, int(curr**0.5) + 1):
        if is_prime(i):
            return i

# Test the function
import unittest

class TestPrimeFib(unittest.TestCase):
    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)
        self.assertIsNone(prime_fib(0))
        self.assertIsNone(prime_fib(-1))

if __name__ == '__main__':
    unittest.main()
```

This script defines the `prime_fib` function and tests it using unittest. When executed, it will run the tests and print "OK" if all tests pass.  If the tests fail, it will print details about the specific tests that failed.  This will help you ensure that your function is working correctly. 
The `is_prime` function is used to check if a number is prime, and the `prime_fib` function uses a Fibonacci search to generate the n-th Fibonacci number that is also prime.  The `unittest` module is used to define a test case and a collection of unit tests.  The `test_prime_fib` method defines specific tests for the `prime_fib` function, checking if it returns the expected values for different inputs.  The `assertEqual` method checks if the actual output of `prime_fib` matches the expected value for each test case.  The `assertIsNone` method checks if the output from `prime_fib` is None for invalid inputs.  Finally, `unittest.main()` is called to run all the defined tests.