Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be positive")
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    while count < n:
        # Check if the next Fibonacci number is prime
        if is_prime(a):
            return a
        
        # Calculate the next Fibonacci number
        b = a + b
        a = b
        count += 1
    
    # If we reach this line, it means the requested number n is out of range
    return -1

# Testing the function
# Using unittest for testing
import unittest

class TestPrimeFib(unittest.TestCase):
    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)
        self.assertEqual(prime_fib(6), -1) 

if __name__ == '__main__':
    unittest.main()
```

This script defines a function `prime_fib` that uses the Fibonacci sequence to generate prime numbers. It then tests this function against a set of known inputs to ensure it performs as expected. 

The `is_prime` function is also provided to check if a given number is prime. 
The `TestPrimeFib` class uses `unittest.main()` to discover all the test cases and run them. 

Note: The `prime_fib` function may not be efficient for larger values of `n` since it iterates through the Fibonacci sequence until it finds the n-th prime Fibonacci number. Alternatively, you can set a maximum limit for n where the function will be allowed to run, and return a responsive message for values above that limit.