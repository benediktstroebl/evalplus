def fibfib(n):
    # Handle special cases (similar to Fibonacci)
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Use a recursive approach
    # Each recursive call eliminates the two last elements of the sequence
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)