

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
    if n <= 1:
        return 2
    else:
        n_1 = 1
        n_2 = 2
        for i in range(2,n):
            n_3 = n_1 + n_2
            n_1 = n_2
            n_2 = n_3
        if is_prime(n_3):
            return n_3
        else:
            return prime_fib(n
