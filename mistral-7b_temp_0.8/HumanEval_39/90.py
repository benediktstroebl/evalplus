

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

    if n <= 1:
        return n

    prime_fib_numbers = set()
    for i in range(2, n + 1):
        if is_fib(i) and is_prime(i):
            prime_fib_numbers.add(i)

    return prime_fib_numbers

