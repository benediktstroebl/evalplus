

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
        return 2, 1
    
    if n in [2, 3]:
        return n, 1
    
    d = 1
    a = 0
    b = 1
    for i in range(2, n):
        if n % i == 0:
            break
        a = b
        b = a + b
        d += b
    
    result = d - 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            continue
        for j in range(i, int(n ** 0.5) + 1):
            if j % i == 0:
                continue
        result = max(result, i)
    
    return result, a - 1
