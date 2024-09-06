
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
    n = len(array)
    # use a helper variable to track the sum of all elements
    total = sum(array)
    # use a helper variable to track whether we should sort in ascending or descending order
    sort_order = total % 2 == 0
    # sort the array and maintain the current sum
    array = sorted(array)
    # update the total
    total = sum(array)
    if sort_order:
        # sort in ascending order
        array = array[::-1]
    return array