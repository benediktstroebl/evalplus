

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n <= 0:
        return 0
    
    # Create a variable to store the last two values in the sequence
    last_two_values = [0, 1]
    
    # Use recursion to compute the n-th element of the sequence
    for i in range(n-1, 0, -1):
        # Create a variable to store the current value
        value = 0
        # Use recursion to compute each of the three sub-sequences
        for j in range(i, 0, -1):
            value = last_two_values[j] + value
        last_two_values.append(value)
        
        # Use slicing to store the last two values in a list
        last_two_values = last_two_values[:-1]
        
    # Add the last two values to get the n-th element of the sequence
    return last_two_values[-1]
