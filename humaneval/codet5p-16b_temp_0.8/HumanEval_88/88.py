
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
        return array
    if len(array) == 1:
        return array
    if len(array) == 2:
        if sum(array)%2 == 0:
            return [array[1], array[0]]
        else:
            return [array[0], array[1]]
    n = len(array)
    l = []
    for i in range(1, n, 2):
        l.append(array[i])
    for i in range(0, n, 2):
        l.append(array[i])
    return l
