
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
    if len(array) <= 1:
        return array
    start = 0
    end = len(array) - 1
    is_even = array[start] + array[end] % 2 == 0
    while start < end:
        while (array[start] % 2 == 1 or not is_even) and start < end:
            start += 1
        while (array[end] % 2 == 0 or is_even) and start < end:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    return array
