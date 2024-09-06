from itertools import accumulate
def fibfib_iter(n: int):
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    fib = [0, 0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3])
    return accumulate(fib)[-1]
def fibfib(n: int):
    return fibfib_iter(n)