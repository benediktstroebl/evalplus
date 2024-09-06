

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
    prime = [2]

    while len(prime) < n:
        fib.append(fib[-2] + fib[-1])
        if fib[-1] % 2 == 0:
            continue
        for i in range(3, fib[-1] + 1, 2):
            if fib[-1] % i == 0:
                break
        else:
            prime.append(fib[-1])
    return prime[n-1]

