
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
    n = len(array)
    if n == 0:
        return []

    pivot_index = (n - 1) // 2
    pivot = array[pivot_index]

    while pivot_index > 0:
        if pivot + (pivot_index * 2) in array:
            array.remove(pivot + (pivot_index * 2))
            n -= 1
        pivot_index -= 1

    for i in range(n):
        array[i] = min(array[i], k)

    return array