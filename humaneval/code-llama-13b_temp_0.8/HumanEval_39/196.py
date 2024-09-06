

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
    if n == 1:
        return 2
    if n == 2:
        return 3

    previous = 1
    current = 2
    prime = 3
    while True:
        next = previous + current
        previous = current
        current = next

        if is_prime(current):
            prime += 1
        if prime == n:
            return current

