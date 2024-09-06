

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
    for i in range(3, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    i, j = 0, 1
    while j < n + 1:
        if is_prime(fibs[j]):
            i += 1
        if i == j:
            return fibs[j]
        j += 1
