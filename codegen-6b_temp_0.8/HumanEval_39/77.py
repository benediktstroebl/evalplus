

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
    while fib[len(fib) - 2] <= n:
        fib.append(fib[len(fib) - 2] + fib[len(fib) - 1])
    for i in fib:
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1 and i != 1:
                return i
    return "error"