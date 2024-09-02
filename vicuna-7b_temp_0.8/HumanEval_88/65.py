
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
        return []

    # sort_array([]) is not a problem but sort_array([1]) is a problem, so
    # we check the length of the array and the first element is not 0
    if len(array) > 1:
        for i in range(1, len(array)):
            # sum(first index value, last index value)
            val = sum(array[i - 1], array[i])
            if val % 2 == 0:
                array.insert(0, array.pop(i))
            else:
                array.insert(0, array.pop(i))
    return array