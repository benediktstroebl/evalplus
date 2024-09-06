

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
    fibs = [1, 1]
    i = 2
    while len(fibs) < n:
        fibs.append(fibs[i - 2] + fibs[i - 1])
        i += 1

    p = 1
    for f in fibs:
        if prime(f):
            p = f
            break

    return p
