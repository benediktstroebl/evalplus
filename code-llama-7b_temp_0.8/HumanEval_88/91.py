
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
    if len(array) == 0:
        return []

    is_ascending = sum(array[0], array[-1]) % 2 != 0

    for idx, value in enumerate(array):
        if idx == 0:
            min_val = value
        else:
            min_val = min(min_val, value)

    for idx, value in enumerate(array):
        if is_ascending:
            array[idx] = min_val - value
        else:
            array[idx] = value - min_val

    if is_ascending:
        array = sorted(array, reverse=True)

    for idx, value in enumerate(array):
        if is_ascending:
            array[idx] = min_val - value
        else:
            array[idx] = value - min_val

    return array
