
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
    first_index = 0
    last_index = len(array) - 1

    if sum(array[0:first_index]) % 2 == 0 and sum(array[last_index:]) % 2 == 1:
        array = sorted(array[:last_index + 1])
    elif sum(array[0:first_index]) % 2 == 1 and sum(array[last_index:]) % 2 == 0:
        array = sorted(array[:first_index]) + sorted(array[last_index:])
    return array

