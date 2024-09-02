
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
    # Check for empty array.
    if not array:
        return []
    # Check for array with one element.
    if len(array) == 1:
        return array
    # Check for array with two elements.
    if len(array) == 2:
        if (array[0] + array[1]) % 2:
            return [array[1], array[0]]
        else:
            return array
    # Create an empty array.
    sorted_array = []
    # For each element, check if the sum of the first and last index is odd or even and populate the new array
    # accordingly.
    if (array[0] + array[-1]) % 2:
        while len(array):
            sorted_array.append(array.pop(0))
    else:
        while len(array):
            sorted_array.append(array.pop(-1))
    return sorted_array
