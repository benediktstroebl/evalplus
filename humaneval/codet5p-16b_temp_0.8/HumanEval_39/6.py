

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

    i = 0
    j = 1
    k = 0
    if n == 1:
        return 2
    while k < n:
        i = j
        j = k
        k = i + j
        if k > 1:
            for m in range(2, k):
                if k % m == 0:
                    break
            else:
                return k

