from collections import deque
def prime_fib(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    fib = deque([0, 1])
    for _ in range(n - 2):
        next_fib = fib[-1] + fib[-2]
        fib.appendleft(next_fib)
        if next_fib == 2:
            continue
        for num in range(3, int(next_fib**0.5) + 1, 2):
            if next_fib % num == 0:
                break
        else:
            return next_fib
    
    return -1