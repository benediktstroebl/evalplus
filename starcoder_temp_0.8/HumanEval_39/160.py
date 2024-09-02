

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
    fib_seq = fibonacci_generator()
    fib_prime = get_fib_prime_generator()
    result = next(fib_prime)
    for i in range(n):
        fib = next(fib_seq)
        if is_prime(fib):
            result = fib
    return result
