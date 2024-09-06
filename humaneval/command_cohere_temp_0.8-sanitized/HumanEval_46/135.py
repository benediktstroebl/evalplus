def fib4(n: int):
    prev = [0, 0, 2, 0]
    current = [0, 0, 0, 0]
    for i in range(n):
        next = [prev[j] + current[j] for j in range(4)]
        prev, current = current, next
    return current[0]