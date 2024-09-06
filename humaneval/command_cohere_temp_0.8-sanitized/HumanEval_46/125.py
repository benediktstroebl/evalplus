def fib4(n: int):
    prev = [0, 0, 2, 0]
    current = [0, 0, 0, 0]
    for i in range(n):
        next = [x + y for x, y in zip(current, prev)]
        prev, current = current, next
    return current[0]