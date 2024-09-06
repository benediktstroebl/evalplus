

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
    F_prev = 1
    F_curr = 1
    F_next = 2

    while n > 0:
        if is_prime(F_next):
            n -= 1
        F_prev, F_curr, F_next = F_curr, F_next, F_next + F_curr

    return F_next

