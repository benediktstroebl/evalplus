

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
    for i in count(2):
        f1, f2 = fib(i-1), fib(i)
        if is_prime(f1) and is_prime(f2):
            if i == n:
                return f1
            elif i > n:
                return f2
