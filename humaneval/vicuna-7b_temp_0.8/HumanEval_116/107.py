
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # Keep track of the number of 1's in the current and next number
    current_ones = 0
    next_ones = 0

    # Start iterating through the array
    for i in range(len(arr)):
        # Update the current and next number's ones count
        current_ones = (arr[i] >> 1).bit_length()
        next_ones += (arr[i+1] >> 1).bit_length()

        # If the next number has more ones, swap the current and next number
        if next_ones > current_ones:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # Swap the last number if it has more ones than the previous number
    if current_ones < len(arr) - 1:
        arr[len(arr)-1], arr[len(arr)-2] = arr[len(arr)-2], arr[len(arr)-1]

    return arr