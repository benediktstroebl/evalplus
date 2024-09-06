
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
        return [0]
    for i in range(1, n):
        for j in range(i):
            if array[j] > array[i]:
                swap = array[j]
                array[j] = array[i]
                array[i] = swap
        if array[0] > array[n-1]:
            n = n-1
        if array[n-2] > array[n-1]:
            n = n-2
    return array