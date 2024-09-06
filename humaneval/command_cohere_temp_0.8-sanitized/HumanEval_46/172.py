def fib4(n: int):
    if n < 0:
        raise ValueError("Fib4 is defined only for positive integers")
    elif n < 4:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)