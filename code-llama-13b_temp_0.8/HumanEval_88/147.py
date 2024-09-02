
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
    if len(array) == 0 or len(array) == 1:
        return array

    i = 0
    j = len(array) - 1
    result = list(array)

    while i < j:
        if sum(result[i:j + 1]) % 2 == 0:
            result[i:j + 1] = sorted(result[i:j + 1], reverse=True)
            i += 1
            j -= 1
        else:
            result[i:j + 1] = sorted(result[i:j + 1])
            i += 1
            j -= 1

    return result
