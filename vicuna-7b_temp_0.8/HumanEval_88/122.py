
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
    result = list(array)
    size = len(array)
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if i + j < size:
                if array[i + j] < array[i]:
                    result[i], result[i + j] = result[i + j], result[i]
                elif array[i] > array[i + j]:
                    result[i], result[i + j] = result[i + j], result[i]
                elif (array[i] + array[i + j]) % 2 == 0:
                    result[i], result[i + j] = result[i + j], result[i]
    return result
