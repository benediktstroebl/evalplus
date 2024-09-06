def fib4(n: int) -> int:
    F = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]
    if n < 3:
        return n
    else:
        return (fib4(n - 1) + fib4(n - 2) + fib4(n - 3)) ** 2