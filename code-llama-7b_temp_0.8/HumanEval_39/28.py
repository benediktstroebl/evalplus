

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
    i = 1
    last = 1
    while True:
        current = last + i
        if is_prime(current):
            if i == 2:
                return current
            else:
                i += 1
        else:
            last = current

