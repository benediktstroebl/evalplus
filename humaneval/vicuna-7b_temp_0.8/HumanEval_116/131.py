
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
    # If the array is empty or one-element, return it
    if not arr:
        return arr

    # If the array has one element, return it
    if len(arr) == 1:
        return arr[0]

    # Initialize a variable for the running sum of the array
    running_sum = 0

    # Initialize a variable for the index of the first non-positive element
    non_positive_index = 0

    # Iterate over the array
    for i in range(len(arr)):
        # Check if the current element is positive
        if arr[i] > 0:
            # Check if the array has more positive elements than the current element
            if len(arr) - non_positive_index > 0 and arr[non_positive_index] > 0:
                # If so, subtract the sum of the previous positive elements
                running_sum -= arr[non_positive_index - len(arr) + 1]
                non_positive_index -= len(arr)
            # Otherwise, the current element is the first positive element
            else:
                # Update the sum of the array
                running_sum += arr[i]
                # Update the index of the first non-positive element
                non_positive_index = i

    # Return the array sorted by the number of ones in its binary representation
    return [running_sum] + arr[non_positive_index:]