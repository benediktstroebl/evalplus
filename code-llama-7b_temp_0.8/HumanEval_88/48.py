
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
    #Check if array is empty
    if not array:
        return []

    #Check if len(array) == 1
    if len(array) == 1:
        return array

    #Check if len(array) > 1
    if len(array) > 1:
        #Get the sum of the first and last value in array
        sum_of_first_and_last = array[0] + array[-1]

        #Check if sum(first value, last value) is odd
        if sum_of_first_and_last % 2 != 0:
            array.sort()
        #Check if sum(first value, last value) is even
        if sum_of_first_and_last % 2 == 0:
            array.sort(reverse=True)
        return array
