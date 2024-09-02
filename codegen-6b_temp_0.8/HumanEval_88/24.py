
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
    if len(array) < 2:
        return array
    if len(array) == 2:
        return sorted(array)

    pivot = array[0] + array[-1]
    if len(array) % 2 == 0:
        pivot /= 2

    count = 0
    for index, val in enumerate(array):
        if val > pivot:
            count += 1

    return array[count:] + array[:count]

