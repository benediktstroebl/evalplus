Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # Initialize the Fibonacci sequence with the first two prime numbers
    fib = [2, 3]
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        if is_prime(next_fib):
            fib.append(next_fib)
        else:
            # Skip non-prime Fibonacci numbers
            pass
    
    return fib[n - 1]

# Test the prime_fib function
def test_prime_fib():
    """
    Tests for the prime_fib function
    """
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89

# Run the tests
test_prime_fib()
```

This script defines the `prime_fib` function, which calculates the n-th Fibonacci number that is also prime. It does this by maintaining a list (`fib`) of Fibonacci numbers and checking each number for primality as it iterates through the sequence. Non-prime Fibonacci numbers are skipped. The `is_prime` function is provided to simplify the primality check. The `test_prime_fib` function contains test cases to verify the correctness of the `prime_fib` function.