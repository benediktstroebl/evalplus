

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    table = [1, 1]
    for i in range(2, n+1):
        table.append(table[i-1] + table[i-2])
    return table[n]
