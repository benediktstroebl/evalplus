

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

    fib = [1, 2]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    i = n
    while True:
        if i == 0:
            break
        i -= 1
        if not is_prime(fib[i]):
            fib.pop()
            break
    return fib[n - 1]

