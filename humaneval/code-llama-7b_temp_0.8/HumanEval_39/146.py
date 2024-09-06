

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
    fibs = [1, 2, 3]

    if n == 1:
        return 2
    elif n == 2:
        return 3

    fib = fibs[-1] + fibs[-2]
    fibs.append(fib)
    while not is_prime(fib):
        fib = fibs[-1] + fibs[-2]
        fibs.append(fib)

    return fib

