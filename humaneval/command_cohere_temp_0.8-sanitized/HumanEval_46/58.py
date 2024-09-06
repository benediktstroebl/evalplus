def fib4(n):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        raise ValueError("fib4 is not defined for negative numbers")
    while len(fib4_cache) <= n:
        fib4_cache.append(fib4_cache[-1] + fib4_cache[-2] + fib4_cache[-3] + fib4_cache[-4])
    return fib4_cache[n]