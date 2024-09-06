

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Add your code here
    if n == 1 or n == 0:
        return n
    
    fib_n_1 = 0
    fib_n_2 = 1
    
    for i in range(n-2):
        fib_n = fib_n_1 + fib_n_2
        fib_n_1 = fib_n_2
        fib_n_2 = fib_n
    return fib_n
    
