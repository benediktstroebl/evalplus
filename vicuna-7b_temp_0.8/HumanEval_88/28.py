
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
    mid = n // 2
    p = array.copy()
    i = 0
    j = mid
    while i < mid:
        if (p[i] + p[j]) % 2 == 0:
            j += 1
        elif (p[i] + p[j]) % 2 == 1:
            i += 1
        else:
            break
    if mid == 0:
        return p.copy()
    mid += 1
    j = mid
    i = mid
    while i < n and j < n:
        if (array[i] + array[j]) % 2 == 0:
            array[i] = array[i] + array[j]
            i += 1
            j += 1
        elif (array[i] + array[j]) % 2 == 1:
            array[j] = array[i]
            i += 1
        else:
            array[j] = array[j] + array[i]
            j += 1
            i += 1
    return array