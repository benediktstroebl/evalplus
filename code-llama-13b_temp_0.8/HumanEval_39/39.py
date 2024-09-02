

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
    first, second = 0, 1
    prime_counter = 0
    while prime_counter < n:
        first, second = second, first + second
        if is_prime(second):
            prime_counter += 1
    return second

