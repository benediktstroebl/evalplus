

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
    # first 5 numbers are 0, 1, 1, 2, 3, we skip first 5 numbers
    if n < 6:
        return 0
    # check if number is prime
    if n % 2 == 0:
        return 0
    if n % 3 == 0:
        return 0
    # check if it's a Fibonacci number
    fib_num = fib(n-1)
    if fib_num == n-1:
        return 0
    else:
        fib_num_2 = fib(n-2)
        if fib_num_2 == n-2:
            return fib_num * fib_num_2
        else:
            return fib_num * fib_num_2 + fib_num_2
