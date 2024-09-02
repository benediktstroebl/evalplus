

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
    if n < 2:
        return None

    result = 2
    fib = 1

    for _ in range(n - 1):
        (result, fib) = (fib, result + fib)

    # if result is prime, return it, otherwise calculate next prime.
    if is_prime(result):
        return result
    return prime_fib(n + 1)

