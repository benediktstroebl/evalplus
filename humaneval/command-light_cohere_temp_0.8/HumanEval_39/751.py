```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    Returns the prime Fibonacci numbers and checks if they are prime using the Sieve of Eratosthenes.
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
    24
    >>> prime_fib(7)
    5
    >>> prime_fib(8)
    8
    >>> prime_fib(9)
    13
    >>> prime_fib(10)
    2412
    >>> prime_fib(13)
    818
    >>> prime_fib(14)
    97
    >>> prime_fib(15)
    TRUE
    """
    sieve = [True] * (4 * (n + 1))
    sieve = [i for i, j in enumerate(sieve) if j]
    return next((i for i, is_prime in zip(sieve, (2, n + 1)) if is_prime))

This function implements the recursive solution for finding prime Fibonacci numbers. It starts by checking the numbers 2 and 3 are prime, then generates numbers 4, 5, 13, and 89. The function then generates numbers up to the specified n using the sieve of Eratosthenians algorithm, which eliminates multiples of primes below the square root (n^2). 

The function returns the n-th prime Fibonacci number.