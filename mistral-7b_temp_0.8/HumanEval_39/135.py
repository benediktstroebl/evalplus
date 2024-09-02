

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
    if n == 1:
        return fib[0]
    if n == 2:
        return fib[1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
        if fib[-1] % 2 != 0:
            fib[-1] = fib[-1] + 1
        if not is_prime(fib[-1]):
            fib.pop()
            fib.append(fib[-1] - 1)
    return fib[-1]

