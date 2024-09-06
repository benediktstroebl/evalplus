

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
    # Handle the base cases
    if n < 2:
        return 2
    elif n < 4:
        return 3
    # Handle the recursive case
    else:
        # Check if n-1 is prime
        if not is_prime(n-1):
            return 2 * prime_fib(n-1)
        # Check if n-2 is prime
        if not is_prime(n-2):
            return 3 * prime_fib(n-2)
        # Compute the n-th Fibonacci number
        fib = 13 * (n - 1)
        # Check if fib is prime
        if not is_prime(fib):
            return 2 * prime_fib(n-1) * prime_fib(n-2)
        # Check if fib is greater than n
        if fib > n:
            return 2 * prime_fib(n-1) * prime_fib(n-2) * (fib // (n-1))
        # Return the n-th number that is a Fibonacci number and it's also prime
        return fib
