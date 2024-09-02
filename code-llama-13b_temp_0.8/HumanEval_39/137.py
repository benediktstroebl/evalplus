

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
    if not isinstance(n, int):
        raise TypeError('n should be of type int')
    if n < 0:
        raise ValueError('n should be a positive integer')
    elif n == 0:
        return 0

    fibs = [0, 1]
    i = 2
    while len(fibs) < n:
        fibs.append(fibs[i-1] + fibs[i-2])
        i += 1

    for i in reversed(range(2, len(fibs))):
        if not is_prime(fibs[i]):
            del fibs[i:]
            break

    return fibs[-1]

