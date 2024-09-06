
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
    if not array:
        return array
    
    # make a copy of the list
    copy = list(array)
    # set the first number to the sorted value, then shift the list
    # if the total is odd, sort ascending, if it's even sort descending
    copy[0] = (sum(copy[:2]) % 2) and sorted(copy[:2])[0] or sorted(copy[:2])[1]
    copy = copy[1:]
    return copy
