

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
    if n <= 0:
        return 2
    first, second = 2, 1
    prime = 2
    while prime < n:
        next = first + second
        prime = 2
        while prime < next:
            if next % prime == 0:
                break
            prime += 1
        if prime == next:
            first, second = second, next
            prime = 2
    return next

