
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
        return []

    if len(array) == 1:
        return array

    first_index = 0
    last_index = len(array) - 1
    for i in range(first_index, last_index + 1):
        if (array[i] % 2 == 0 and array[i] + array[last_index] >= array[last_index] + array[i] or
            array[i] % 2!= 0 and array[i] + array[first_index] <= array[first_index] + array[i]):
            first_index = i

    for i in range(last_index, first_index, -1):
        if (array[i] % 2 == 0 and array[i] + array[last_index] >= array[last_index] + array[i] or
            array[i] % 2!= 0 and array[i] + array[first_index] <= array[first_index] + array[i]):
            last_index = i

    sorted_array = [None] * len(array)
    
