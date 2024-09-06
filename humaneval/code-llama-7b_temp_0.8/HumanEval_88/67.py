
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
    # Special case
    if len(array) == 0: return []

    # Loop over the array
    index = 0
    while index < len(array) - 1:
        # If the next element is smaller or equal to the current one, we keep going
        if array[index] <= array[index+1]:
            index += 1
        else:
            # If the next element is bigger than the current one, we swap
            array[index], array[index+1] = array[index+1], array[index]
            # Then we keep looping
            continue
    # If the sum is odd, return the array in ascending order
    if sum(array[0]) + sum(array[len(array) - 1]) % 2 == 1:
        return array
    # If the sum is even, return the array in descending order
    else:
        return array[::-1]
