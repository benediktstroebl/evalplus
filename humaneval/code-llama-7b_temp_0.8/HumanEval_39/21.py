

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
        return -1

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    i = 1
    result = -1

    while i <= n:
        i += 1
        if is_prime(fib(i)):
            result = fib(i)
            n -= 1
        if n == 0:
            break

    return result

