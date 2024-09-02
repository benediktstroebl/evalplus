

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

    # Practice using an exception
    if n < 0:
        raise Exception("Negative index")

    # There are no prime Fibonacci numbers with indexes less than or equal to 1
    if n <= 1:
        return 0

    f_previous = 1
    f_current = 1

    index = 1

    while True:

        f_next = f_previous + f_current

        f_previous = f_current
        f_current = f_next

        index += 1

        if is_prime(f_current) == True:
            if index == n:
                return f_current

