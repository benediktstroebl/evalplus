

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
    # Base cases
    if n == 1:
        return 2
    elif n == 2:
        return 3
    if n < 2:
        raise ValueError('input should be > 2')
    fib_list = [2, 3]
    # Finding the n-th fib number
    while True:
        fib_num = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_num)
        if len(fib_list) == n:
            return fib_num

