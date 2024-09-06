
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
    if n == 1:
        return [array[0]]

    left = 0
    right = n - 1
    i = 0
    while i < n:
        while i <= right and array[i] <= array[i + 1]:
            i += 1
        while i < left and array[i] >= array[i - 1]:
            i -= 1

        for j in range(i, right):
            array[j], array[i] = array[i], array[j]

        for j in range(left, i):
            array[j], array[i] = array[i], array[j]

        i += 1

    return array