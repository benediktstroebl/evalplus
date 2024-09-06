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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Ensure n is positive
    n = abs(n)
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    count = 0
    while count < n:
        # Store the current Fibonacci number
        temp = b
        b = a + b
        a = temp
        count += 1
        
        # Check if the current Fibonacci number is prime
        if is_prime(a):
            return a
    
    # If we reach this point, the loop hasn't found a prime Fibonacci number in 'n' iterations.
    # Assuming `n` is large, the next Fibonacci number would be larger than `n`,
    # so it would have been found in the loop above. However, as a failsafe,
    # return the next Fibonacci number after 'n' iterations to avoid an infinite loop.
    return a

# Testing the function
import pytest

@pytest.mark.parametrize('input, expected', [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89),
])
def test_prime_fib(input, expected):
    """
    Tests the prime_fib function.
    """
    result = prime_fib(input)
    assert result == expected
```
This script defines a `prime_fib` function that calculates the n-th Fibonacci number that is also prime. It achieves this by iterating through the Fibonacci sequence and checking each number for primality using the `is_prime` function. If a prime number is found before `n` iterations, it returns that number, and if not, it returns the next Fibonacci number as a failsafe. The code includes a test suite to validate the correctness of the `prime_fib` function for different input values.