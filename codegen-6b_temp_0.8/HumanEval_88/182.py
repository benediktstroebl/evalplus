
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
    length = len(array)
    if length == 0:
        return []
    if length == 1:
        return array

    #Convert array into 1D
    one_d = []
    for i in range(length):
        one_d.append(array[i])

    #Sort 1D array
    one_d.sort(reverse=True)

    #Convert back to 2D
    array = []
    for i in range(length):
        array.append(one_d[i])

    return array
