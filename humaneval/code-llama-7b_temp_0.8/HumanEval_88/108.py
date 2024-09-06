
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Check for edge case
    if not array:
        return array
    # Get the first and last element
    first, last = array[0], array[-1]
    # Check if the sum is even or odd
    if (first + last) % 2 == 0:
        # Get the odd length of the array
        odd_length = len(array) // 2
        # Sort the first half of the array
        # array[:odd_length] = sorted(array[:odd_length])
        # Sort the second half of the array
        # array[odd_length:] = sorted(array[odd_length:])
        # Merge the two parts of the array
        return _merge(sorted(array[:odd_length]), sorted(array[odd_length:]))
    # Sort the two parts of the array
    return _merge(sorted(array[:odd_length]), sorted(array[odd_length:]))

