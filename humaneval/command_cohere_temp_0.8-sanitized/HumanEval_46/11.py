def fib4(n):
    prev = [0, 0, 2, 0]
    for _ in range(4, n + 1):
        curr = prev[-1] + prev[-2] + prev[-3] + prev[-4]
        prev.append(curr)
    return prev[-1]