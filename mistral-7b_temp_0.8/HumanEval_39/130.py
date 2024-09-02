

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
    fib = [1, 1]
    fib_len = len(fib)
    for i in range(2, n):
        fib_len += 1
        fib.append(fib[-1] + fib[-2])
        if fib_len > n:
            break
    while not is_prime(fib[-1]):
        fib_len -= 1
        fib.pop(-1)
        if fib_len == 1:
            return fib[0]
    return fib[-1]

