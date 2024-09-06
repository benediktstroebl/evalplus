

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
    if n <= 1:
        return n

    if n in [2, 3]:
        return n

    is_prime = True
    p = 2
    q = 1
    f = 1
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            is_prime = False
            break
        p *= i + 1
        q *= i

    if is_prime:
        return p
    else:
        for i in range(q, n, 2):
            if (p - i + q) % i == 0:
                is_prime = False
                break
        if is_prime:
            return p
        else:
            return p - q + 1
