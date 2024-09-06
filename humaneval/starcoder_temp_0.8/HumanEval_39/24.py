

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
    elif n == 2:
        return 3
    else:
        n_1 = 2
        n_2 = 3
        count = 3
        while count <= n:
            next = n_1 + n_2
            n_2 = n_1
            n_1 = next
            count += 1
            if is_prime(next):
                return next

