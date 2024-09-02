
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

    if len(array) < 2:
        return array

    return_array = [0 for _ in array]
    for i in range(1, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if sum(array[j], array[j + 1]) % 2 == 0:
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
            else:
                if array[j] < array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

    return return_array
