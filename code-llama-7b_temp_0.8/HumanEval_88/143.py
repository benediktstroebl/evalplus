
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

    # arr_sum = sum(array)
    # if arr_sum % 2 == 0:
    #     # sort in ascending order
    #     array.sort()
    # else:
    #     # sort in descending order
    #     array.sort(reverse=True)

    # # odd or even
    # if arr_sum % 2 == 0:
    #     return array

    # # odd
    # else:
    #     return array[::-1]

    arr_sum = sum(array)
    is_odd = arr_sum % 2 == 1
    arr_sorted = sorted(array) if is_odd else sorted(array, reverse=True)
    return arr_sorted


