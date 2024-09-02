

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

    assert n >= 1
    i = 2
    f = [1, 1]
    while i < n:
        f.append(f[-1] + f[-2])
        i += 1
        if not all(f % i!= 0 for i in range(2, f[-1] // 2 + 1)):
            f[-1] += 1
            i -= 1
    return f[-1]
