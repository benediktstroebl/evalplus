def f(n):
    return [0] * int(n/2) + [factorial(i) if i % 2 == 0 else sum(range(1, i + 1)) for i in range(1, n)]