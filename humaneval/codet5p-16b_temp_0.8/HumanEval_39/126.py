

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

    fib_0, fib_1 = 0, 1
    fib_2 = 0
    prime_nums = []
    while len(prime_nums)!= n:
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        fib_2 = fib_0 + fib_1
        if (fib_2 % 2 == 0 and fib_2 % 3!= 0) or fib_2 < 4:
            prime_nums.append(fib_2)
    return prime_nums[-1]

