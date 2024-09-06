

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
    if n < 1:
        raise ValueError

    # first 10 fibonacci numbers
    fib_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # fibanacci number of n
    fib = fib_list[n - 1] + fib_list[n - 2]

    # check if it's prime
    for divisor in range(2, fib):
        if fib % divisor == 0:
            return False
        if divisor > fib / divisor:
            return True

