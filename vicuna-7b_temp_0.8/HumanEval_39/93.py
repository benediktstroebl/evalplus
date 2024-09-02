

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
    if n < 2:
        return 2
    if n == 2:
        return 3

    fib_list = [0, 1, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    for i in range(n-1, -1, -1):
        if fib_list[-1] % i:
            return i

    return n
