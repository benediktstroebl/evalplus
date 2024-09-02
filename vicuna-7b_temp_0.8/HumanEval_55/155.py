

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 0, 1
    for i in range(n):
        if i == 0 or i == 1:
            yield a
        a, b = b, a + b

fib_iter = fib(100)

for i, a in enumerate(fib_iter):
    print(i)