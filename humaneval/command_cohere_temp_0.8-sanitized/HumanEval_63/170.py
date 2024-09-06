def fibfib(n):
    # Create an array to store the previously calculated values for the FibFib sequence
    fibfib_array = [0, 0, 1]

    # Initialize the first two elements (0 and 1) of the array by setting fibfib(0) and fibfib(1) to 0 and 1 respectively
    fibfib_array[0] = 0
    fibfib_array[1] = 1

    # Start loop from 2, since the first two elements have already been initialized
    for i in range(2, n + 1):
        # Set the current value of the sequence to the sum of the last 3 values in the array (up to array's length)
        fibfib_array[i] = fibfib_array[i - 1] + fibfib_array[i - 2] + fibfib_array[i - 3]

    # Return the value of the nth FibFib number
    return fibfib_array[n]