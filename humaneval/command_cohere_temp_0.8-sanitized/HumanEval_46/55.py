def fib4(n: int):
    if n < 0:
        raise ValueError(" fib4 is not defined for negative numbers")
    elif n < 4:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)