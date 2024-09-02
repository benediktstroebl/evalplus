

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
    elif n == 2:
        return 3
    else:
        for i in range(2, int(n**0.5) + 1):
            for j in range(i + 1, n):
                if is_prime(j) and j - i == 1:
                    return j
        return None
