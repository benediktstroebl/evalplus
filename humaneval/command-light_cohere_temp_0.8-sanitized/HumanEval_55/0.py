def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)