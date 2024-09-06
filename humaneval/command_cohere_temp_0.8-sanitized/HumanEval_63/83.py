def fibfib(n):
    # Handle special cases
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Use dynamic programming to avoid redundant computations
    fib = [0, 0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    
    return fib[n]