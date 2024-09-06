def fibfib(n):
    # Create an array to store fibfib values for future computations
    fibfib_array = [0, 0, 1]
    if n >= len(fibfib_array):
        for _ in range(n-len(fibfib_array) + 1):
            fibfib_array.append(fibfib_array[-1] + fibfib_array[-2] + fibfib_array[-3])
    return fibfib_array[n]