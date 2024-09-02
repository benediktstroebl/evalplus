
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
    i = 0
    j = 0
    count = 0
    while i < n:
        if count % 2 != 0:
            for j in range(i, n):
                array[j], array[i] = array[i], array[j]
                count += array[i] + array[j]
        else:
            for j in range(i, n):
                array[j], array[i] = array[i], array[j]
                count += array[i] + array[j]
        i += 1
        j += 1
        count += array[i] + array[j]
    return array
