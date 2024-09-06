

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Check if the input is positive
    if n < 1:
        return 0

    # Initialize the running sum with 1
    running_sum = 1

    # Iterate through the numbers from 1 to n
    for i in range(1, n+1):
        # Add the current number to the running sum
        running_sum += i

    # Return the running sum
    return running_sum
