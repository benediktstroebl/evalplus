
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

    if not array:
        return array

    size = len(array)
    last = array[-1]

    for i in range(size - 2, -1, -1):
        array[i + 1] = last
        last = array[i]

    mid = size // 2
    if size % 2:
        array[mid] = last
        last = array[mid]
    array[0] = last

    i = 1
    while i < size - 1:
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
        i += 2

    return array
