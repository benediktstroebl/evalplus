
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
    if len(array) <= 1:
        return array

    result = array.copy()
    # Edge case
    result[0] = array[-1]
    result[-1] = array[0]

    # Array contains 1 or more than 1 elements
    i = 0
    j = len(array) - 1

    while i < j:
        sum = result[i] + result[j]
        if sum % 2 == 0:
            # swap elements
            temp = result[j]
            result[j] = result[i]
            result[i] = temp

        i += 1
        j -= 1

    return result
