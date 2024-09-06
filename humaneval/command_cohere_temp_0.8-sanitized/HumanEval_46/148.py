def fib4(n: int, memo={}):
    if n in memo:
        return memo[n]
    a, b, c, d = 0, 0, 0, 0
    for i in range(n):
        a, b, c, d = b + c + d, a + b + c + d, a, a + b
    memo[n] = d
    return d