def fibfib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Utilizing the recursive formula with an optimized iterative approach
    fibfib_prev = 0
    fibfib_curr = 1
    for _ in range(3, n + 1):
        fibfib_next = fibfib_prev + fibfib_curr
        fibfib_prev, fibfib_curr = fibfib_curr, fibfib_next
    
    return fibfib_curr