

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
    for i in range(n - 2):
        fib.append(fib[i] + fib[i + 1])
        
    for i in range(3, len(fib)):
        while not is_prime(fib[i]):
            fib[i] += 1
    return fib[n - 1]

