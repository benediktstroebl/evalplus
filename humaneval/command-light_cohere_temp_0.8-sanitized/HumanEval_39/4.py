def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(2, n + 1):
        a, b = b, a + b
    return a