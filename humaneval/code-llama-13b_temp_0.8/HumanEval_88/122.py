
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
    result = array[:]
    if len(result) < 2:
        return result
    mid = len(result) // 2
    left = result[:mid]
    right = result[mid:]
    left = sort_array(left)
    right = sort_array(right)
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if sum(left[i], right[j]) % 2 == 0:
            if left[i] < right[j]:
                i += 1
            else:
                j += 1
        else:
            if left[i] > right[j]:
                i += 1
            else:
                j += 1
    return left + right

