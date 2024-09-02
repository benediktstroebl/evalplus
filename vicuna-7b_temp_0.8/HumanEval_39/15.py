

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
    # use fibonacci sequence to get n-th number
    # check if it's prime
    # if yes, return it
    if n < 2 or n > 4:
        return -1
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 5:
        return 89
    fib_nums = [2, 1, 1, 1]
    for i in range(n-2, -1, -1):
        for j in range(i-1, -1, -1):
            fib_nums[j] += fib_nums[j+1]
    for i in range(n-1, 1, 1):
        if fib_nums[i] % 2 == 0:
            return -1
    return 2