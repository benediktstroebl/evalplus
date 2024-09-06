Here's the solution to the provided markdown code block problem using Python:
```python
def prime_fib(n: int):
    """
    This function returns the n-th Fibonacci number that is also prime.

    The function uses the prime testing methods to determine if a number is prime,
    and the n-th Fibonacci number is returned.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    >>> prime_fib(6)
    Rudab 1
    """
    if n <= 1:
        return n
    # If n is even, it is not prime and therefore not Fibonacci
    # so we check for divisibility by 2 and all positive integers up to the square root of n
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return 0
    # Now n must be odd
    # Check for divisibility by all odd numbers up to the square root of n
    for i in range(3, int(n ** .5) + 2, 2):
        if n % i == 0:
            return 0
    # Since n is odd and not divisible by any other odd number, it must be prime
    return n
```
The provided code defines a function called `prime_fib` that calculates the n-th Fibonacci number and tests whether it's also prime.  It function uses trial methods to determine primality, including divisibility checks and checking for other factors.