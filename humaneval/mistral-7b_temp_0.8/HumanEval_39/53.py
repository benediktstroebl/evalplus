

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
    assert isinstance(n, int)
    assert n > 0

    f = [1, 1]
    p = 2
    while True:
        # f is n-th Fibonacci number, f = (f_n-2) + (f_n-1)
        f.append(f[-1] + f[-2])

        # p is n-th prime number
        while p * p <= f[-1]:
            if f[-1] % p == 0:
                p += 1
            else:
                break

        if p * p > f[-1]:
            return f[-1]

