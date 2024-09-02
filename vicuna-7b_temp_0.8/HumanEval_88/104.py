
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
    # sort the array
    while (n > 0):
        # if the sum( first index value, last index value) is odd
        if sum(map(lambda x: array[x], range(n-1, n+1))) % 2 == 1:
            # swap the first and last element
            array[0], array[-1] = array[-1], array[0]
            n -= 1
        # if the sum( first index value, last index value) is even
        elif sum(map(lambda x: array[x], range(n-1, n+1))) % 2 == 0:
            # swap the last and second last element
            array[-1], array[-2] = array[-2], array[-1]
            n -= 1
        # if the sum( first index value, last index value) is odd, do nothing
        else:
            n -= 1
    return array