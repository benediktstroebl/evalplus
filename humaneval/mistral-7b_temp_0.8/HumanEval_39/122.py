

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
    a = 1
    b = 1
    while b < n:
        next_num = a + b
        if next_num > n:
            break
        if next_num % 2 == 0:
            b = next_num
        else:
            a = next_num
    return next_num

