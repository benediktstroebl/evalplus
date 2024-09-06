
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

    # create copy of array
    copy_array = array[:]
    # get sum of first and last item
    sum_first_and_last = array[0] + array[-1]
    # sort array
    if sum_first_and_last % 2 != 0:
        copy_array.sort()
    else:
        copy_array.sort(reverse = True)
    return copy_array






























































































































































