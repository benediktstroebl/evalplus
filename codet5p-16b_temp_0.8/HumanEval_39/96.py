

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

    assert n >= 1, "Incorrect input"
    
    fib = [1, 2]
    fib_prime = [2]
    
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
        fib_prime.append(is_prime(fib[i - 1]))
        
    return fib[n] if fib_prime[n] else fib[n] + fib[n - 1]

