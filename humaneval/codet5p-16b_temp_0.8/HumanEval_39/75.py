

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

    last_fib = 1
    fib_nums = [1]
    for i in range(n):
        last_fib, fib_nums[i] = fib_nums[i], last_fib+fib_nums[i]
        if fib_nums[i] > n:
            break
        if is_prime(fib_nums[i]):
            pass
        else:
            return fib_nums[i-1]

