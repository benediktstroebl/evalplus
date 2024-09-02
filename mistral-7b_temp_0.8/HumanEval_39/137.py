

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
    last_prime = 2
    last_fib = 1

    while True:
        if is_prime(last_fib):
            if last_prime < n <= last_fib:
                return last_prime
            last_prime = last_fib

        last_fib = last_fib + last_prime
        last_prime = last_fib - last_prime

