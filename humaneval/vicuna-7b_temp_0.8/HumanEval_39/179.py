

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
    if n < 2 or not (n % 2 == 0):
        return 1
    if n == 2:
        return 2
    if n in [1, 2]:
        return 3
    if n == 3:
        return 5
    limit = int(math.sqrt(n)) + 1
    fib = [0, 1]
    fib_n = [0, 1]
    for i in range(1, limit):
        fib[i] = fib[i - 1] + fib[i - 2]
        fib_n[i] = fib_n[i - 1] + fib_n[i - 2]
    for i in range(10, int(math.sqrt(n))):
        if fib[i] % 2 == 0:
            continue
        if fib[i] == n:
            return 1
        if prime_fib(n // fib[i]) > fib[i]:
            return fib[i]
    return 2
