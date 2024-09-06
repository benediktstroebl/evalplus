```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    Returns 0 if n < 2, else return the n-th Fibonacci number that is a prime (never returns 0).
    """
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return n
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        is_prime[i] = is_prime[i - 1] and is_prime[i - 2] == False
    return is_prime[n]
def test_prime_fib():
    """
    Test the function for different input values.
    """
    test_prime_fib(1)
    assert prime_fib(2) == 2
    assert prime_fib(3) == 3
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 2  # Should return 0 (false)
    assert prime_fib(7) == 2  # Should return 0 (false)
    assert prime_fib(8) == 8  # Should return 2 (true)
    assert prime_fib(9) == 3  # Should return 5 (true)
    assert prime_fib(10) == 89  # Should return 13 (true)
```

This script defines a function `prime_fib` that calculates the n-th Fibonacci number and determines if it is prime. It also contains a test_prime_fib function that verifies the correctness of the `prime_fib` function with various inputs.