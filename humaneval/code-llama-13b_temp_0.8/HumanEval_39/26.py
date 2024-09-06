

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
    fib_nums = [1, 1]
    num = 2
    while len(fib_nums) < n:
        fib_nums.append(num)
        num = fib_nums[-1] + fib_nums[-2]
    return fib_nums[-1]

