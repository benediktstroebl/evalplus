

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
        raise ValueError('Input value must be positive')

    number = 2
    fib = [1, 1]
    while number != n:
        fib.append(fib[-1] + fib[-2])
        number += 1

    if is_prime(fib[-1]):
        return fib[-1]
    else:
        return prime_fib(n-1)

