

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

    f_n = 0
    i = 1
    while i < n:
        f_n += 1
        i += 1
        if is_prime(f_n):
            continue
        else:
            f_n += 1
            i += 1
            if is_prime(f_n):
                continue
            else:
                f_n += 1
                i += 1
                if is_prime(f_n):
                    continue
                else:
                    return f_n
    return f_n

