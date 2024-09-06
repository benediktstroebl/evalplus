def fib4(n: int) -> int:
    bas = [0, 0, 2, 0]
    for i in range(5, n + 1):
        bas.append(bas[i - 1] + bas[i - 2] + bas[i - 3] + bas[i - 4])
    return bas[n]