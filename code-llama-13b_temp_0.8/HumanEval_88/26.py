
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
    # validating the input
    if not isinstance(array, list):
        raise TypeError('The given array must be a list!')
    for num in array:
        if not isinstance(num, int):
            raise TypeError('All the values must be integers!')
        if num < 0:
            raise ValueError('All the values must be non-negative!')
    # sorting the array
    return sorted(array, key=sum)
