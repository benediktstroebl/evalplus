

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
    fib_num, fib_prev, fib_next = 2, 1, 3
    while fib_num < n:
        fib_next = fib_prev + fib_num
        if is_prime(fib_next):
            return fib_next
        else:
            fib_prev, fib_num = fib_num, fib_next
    return fib_next

