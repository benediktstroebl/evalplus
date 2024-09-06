

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

    prime_numbers = prime_fib(n-1) + prime_fib(n-2)
    for num in range(2, int(prime_numbers**0.5) + 1):
        if prime_numbers % num == 0:
            prime_numbers += 2
    return prime_numbers

