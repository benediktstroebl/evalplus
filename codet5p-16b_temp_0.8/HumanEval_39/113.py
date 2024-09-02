

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

    count = 0
    i = 1
    while count!= n:
        fib_num = (i ** 2 + i) / 2
        if is_prime(fib_num) and (i + 2) % 2 == 0:
            count += 1
        i += 1
    return fib_num

