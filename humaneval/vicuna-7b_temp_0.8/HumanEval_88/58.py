
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
    # store the sum of the elements in the first i elements
    # where i is a variable and start from 0
    sum_i = 0
    # store the sum of the elements in the first i elements
    # where i is a variable and start from 0
    sum_j = 0
    for i in range(n):
        sum_i += array[i]
        # check if the sum of the elements in the first i elements
        # is odd or even
        if sum_i % 2 == 1:
            #sort the array in descending order
            array.sort(reverse=True)
        else:
            #sort the array in ascending order
            array.sort()
    return array