
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
    # Check if the array is empty
    if not arr:
        return []
    
    # Initialize the result array
    result = [arr[0]]
    
    # Loop through the array
    for i in range(1, len(arr)):
        # Compare the current element with the pivot element
        if arr[i] > arr[i-1]:
            # If the current element is greater than the pivot, swap it with the pivot
            result[i] = arr[i-1]
            result[i-1] = arr[i]
    
    # Return the sorted array
    return result