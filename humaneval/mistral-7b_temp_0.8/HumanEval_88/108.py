
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
    new_array = []

    new_array = array.copy()

    if len(array) == 1:
        return array

    if array[0] + array[-1] % 2 == 0:
        for i in reversed(range(len(array))):
            new_array.append(array[i])
        return new_array

    for i in range(len(array)):
        new_array.append(array[i])
    return new_array


