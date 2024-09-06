

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n, 1
    elif n == 2:
        return 1, 1
    else:
        return fib(n-1) + fib(n-2)

fib_numbers = [n for n in range(1000)]
for n in fib_numbers:
    print(n, fib(n))