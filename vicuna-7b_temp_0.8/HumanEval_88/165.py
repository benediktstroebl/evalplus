
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
        return [x for x in array]

    if n == 1:
        return [array[0]]

    i, j = 0, n-1
    while i < j:
        while i < j and array[i] <= array[j]:
            i += 1
        while i < j and array[j] >= array[i]:
            j -= 1
    if (j-i) % 2 == 0:
        array[i:j] = [array[i], array[j]]
        return array[i:j+1]
    else:
        array[i:j] = [array[i], array[j]]
        return array[i:j+1]