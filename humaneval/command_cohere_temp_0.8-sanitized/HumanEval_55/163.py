def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    fib_value = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = fib_value
    return fib_value