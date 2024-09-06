

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
    n = n - 1
    if n == 0:
        return 2
    if n == 1:
        return 3
    fib_nums = []
    i = 2
    while len(fib_nums) < n:
        if is_prime(i) and i in fib_nums:
            return i
        fib_nums.append(fib(i))
        i += 1
    return fib(i - 1)

