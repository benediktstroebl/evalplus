

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
        return None

    first = 1
    second = 1
    tmp = 0

    for _ in range(2, n+1):
        tmp = first + second

        if is_prime(tmp):
            first = second
            second = tmp
            continue

        first += 1
        second += 1

    return tmp

