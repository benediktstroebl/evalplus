
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
    # sort by odd or even
    is_even = sum(array[0], array[-1]) % 2 == 0
    for i in range(1, len(array) - 1):
        if array[i] < array[i - 1] and array[i] < array[i + 1]:
            if is_even:
                array[i - 1], array[i + 1] = array[i + 1], array[i - 1]
        else:
            if not is_even:
                array[i - 1], array[i + 1] = array[i + 1], array[i - 1]
    return array

