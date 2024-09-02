

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
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
    """

    if n == 1:
        return 2
    if n == 2:
        return 3

    # Step 1. Compute the n-th Fibonacci number (using function fib).
    n_fib = fib(n)

    # Step 2. Check if number is prime.
    # This is only an optimization, it's slower than first step.
    if is_prime(n_fib):
        return n_fib

    # Step 3. Calculate n-th prime number (using function primes).
    return primes(n)[-1]

