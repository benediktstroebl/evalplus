

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
    prime = 2
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        prime += 1
        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            if fib[-1] == prime:
                return prime
    return fib[n - 1]

