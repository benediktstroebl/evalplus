
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
    # 1. check the given array
    if not array:
        return array

    # 2. find the sum of the first and the last element of the given array
    first_last_sum = array[0] + array[-1]

    # 3. sort it in ascending order if the sum(first index value, last index value) is odd
    if first_last_sum % 2:
        sorted_array = sorted(array)
    # 4. sort it in descending order if the sum(first index value, last index value) is even
    else:
        sorted_array = sorted(array, reverse=True)

    return sorted_array
