

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
    fibs = [2, 3]
    while len(fibs) < n:
        fib = fibs[-1] + fibs[-2]
        if fib > n:
            break
        if is_prime(fib):
            fibs.append(fib)
    return fibs[-1]

