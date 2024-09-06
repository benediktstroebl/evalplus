def fibfib(n):
    # Create an array to store fibfib values and initialize the first three values
    fibfib_array = [0, 0, 1]
    if n <= 3:
        return fibfib_array[n]
    
    # Use dynamic programming to compute fibfib values and return the n-th value
    for i in range(3, n + 1):
        fibfib_array[i] = fibfib_array[i - 1] + fibfib_array[i - 2] + fibfib_array[i - 3]
    
    return fibfib_array[n]