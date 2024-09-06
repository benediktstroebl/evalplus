

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
    fib_nums = [0, 1]
    pfs = [2, 3, 5, 7]
    while True:
        fib_nums.append(fib_nums[-2] + fib_nums[-1])
        for pf in pfs:
            if fib_nums[-1] % pf == 0:
                if pf == 2:
                    return fib_nums[-1]
                else:
                    pfs.append(fib_nums[-1])
                    break

