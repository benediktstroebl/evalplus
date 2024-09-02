

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
    if n < 2:
        raise ValueError("n must be greater than 1")
    
    if n <= 1:
        return 2
    
    fib_list = [0, 1]
    fib_list.append(next(iter(fib_list)))
    fib_list.append(next(iter(fib_list)))
    
    while len(fib_list) < n:
        fib_list.append(next(iter(fib_list)))
    
    for i in range(1, n):
        if fib_list[i] % 2 == 0:
            return 0
    return fib_list[-1]
