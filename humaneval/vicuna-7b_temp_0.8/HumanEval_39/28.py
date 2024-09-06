

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
    if n < 2:
        return 2
    if n < 4:
        return 3
    if n < 100000:
        if is_prime(n-1) and is_prime(n-2) and n-1 < 1000000000:
            return (n-1)*(n-2)
        elif is_prime(n-2):
            return 3*n-2
        elif is_prime(n-1):
            return 5*n-2
        else:
            return 2*n-1
    else:
        return 1
