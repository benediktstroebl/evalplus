def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return _fib(n)
def _fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return _fib(n - 1) + _fib(n - 2)