
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
    # find the first and last element of the array
    first_idx = 0
    last_idx = len(array) - 1

    # compare the sum of the first and last element
    if sum(array[first_idx], array[last_idx]) % 2 == 0:
        # even number
        # sort descending
        # sort the given array in descending order
        array.sort(reverse=True)
    else:
        # odd number
        # sort ascending
        # sort the given array in ascending order
        array.sort()

    return array

    # return array.sort(reverse=True) if sum(array[first_idx], array[last_idx]) % 2 == 0 else array.sort()

