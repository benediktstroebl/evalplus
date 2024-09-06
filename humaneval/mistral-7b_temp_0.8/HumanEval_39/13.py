

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
    if n == 2:
        return 3
    fibs = [2, 3]
    i = 3
    while True:
        if not is_prime(fibs[i]):
            i += 1
            continue
        if len(fibs) == n:
            return fibs[i]
        fibs.append(fibs[i-1] + fibs[i-2])
        i += 1

