
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

    if not array:
        return array

    array_sorted = array[:]
    is_descending = False

    if (sum(array[0], array[-1]) % 2) == 0:
        is_descending = True

    if is_descending:
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
    else:
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return array_sorted

