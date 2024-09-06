
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
    odd_sum = 0
    array_size = len(array)
    result = [0] * array_size

    for i in range(array_size):
        if i == 0:
            odd_sum = array[i]
        elif i == array_size - 1:
            result[i] = array[i]
            odd_sum += array[i]
        else:
            if odd_sum % 2 == 1:
                result[i] = array[i]
            else:
                result[i] = array[i] * -1

    return result

