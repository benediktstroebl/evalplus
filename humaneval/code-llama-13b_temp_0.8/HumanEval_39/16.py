

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
    f1, f2 = 0, 1
    prime_count, count = 0, 0

    while prime_count < n:
        count += 1

        if count % 2 == 0:
            f1 = f1 + f2
        else:
            f2 = f1 + f2

        if is_prime(f2):
            prime_count += 1

    return f2

