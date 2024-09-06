
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

    l = len(array)
    if l <= 1:
        return array
    pivot = 0
    for i in range(l):
        if array[i] > pivot:
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1

    left = pivot
    right = pivot + 1
    while right < l:
        if array[left] < array[right]:
            left += 1
        else:
            array[left], array[right] = array[right], array[left]
            right += 1
    return array

