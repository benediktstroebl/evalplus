

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
    if n < 1:
        return None
    if n == 1 or n == 2:
        return n
    if n > 2 and not is_prime(n):
        return None
    # Found a solution for this recursion
    current_fib = 1
    next_fib = 1
    for _ in range(2, n):
        current_fib, next_fib = next_fib, current_fib + next_fib
    return current_fib
