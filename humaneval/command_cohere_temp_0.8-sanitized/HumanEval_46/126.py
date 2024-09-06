def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        return None
    if n < 5:
        return fib4_cache[n]