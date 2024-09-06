

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
    if n < 3:
        return n
    fibnums = [1, 2]
    while len(fibnums) <= n:
        fibnums.append(fibnums[len(fibnums) - 2] + fibnums[len(fibnums) - 1])

    prime = True
    for num in fibnums:
        if num > 1 and not is_prime(num):
            prime = False

    return fibnums[n] if prime else None

