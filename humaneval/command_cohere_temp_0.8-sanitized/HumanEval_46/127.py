def fib4(n: int):
    fib4_cache = [0, 0, 2, 0]
    if n < 0:
        return "Invalid input: n should be a non-negative integer."
    while len(fib4_cache) <= n:
        fib4_cache.append(fib4_cache[-1] + fib4_cache[-2] + fib4_cache[-3] + fib4_cache[-4])
    return fib4_cache[n]