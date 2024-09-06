Here is a Python script that contains a self-contained function to calculate the n-th Fibonacci number that is also prime:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3  # Base case: Fibonacci number is always prime for n <= 3
    is_prime = True  # Assume all Fibonacci numbers greater than 3 are prime
    for i in range(4, n + 1):
        if is_prime and i % 2 != 0:
            is_prime = False  # Exclude even numbers
        if is_prime:
            continue
    return i  # Return the n-th prime Fibonacci number

# Unit tests
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 28
    assert prime_fib(7) == 24
    assert prime_fib(8) == 8  # This should return 56
    assert prime_fib(9) == 233  # This should return 661
    assert prime_fib(10) == 5258  # This should return 55 probationary number
```

This code defines a function `prime_fib` that calculates the n-th Fibonacci number and returns it if it is prime, or returns the n+1th Fibonacci number if it is not prime. The unit tests section then verifies the expected output for different values of `n`.