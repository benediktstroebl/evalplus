

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
    assert type(n) is int, "prime_fib expects int as n"
    assert n > 0, "prime_fib expects positive n"

    fib_list = [1, 1]
    n -= 2
    while n > 0:
        fib_list.append(fib_list[-1] + fib_list[-2])
        n -= 1
    return fib_list[n]

