
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
    sorted_array = []
    if len(array) <= 1:
        return array
    else:
        for index, value in enumerate(array):
            if index == 0:
                sum1 = value
            elif index == (len(array) - 1):
                sum2 = value
            else:
                sum1 = sum1 + value
                sum2 = sum2 + value
        if (sum1 + sum2) % 2 != 0:
            for index, value in enumerate(array):
                sorted_array.append(value)
            return sorted(sorted_array, reverse=True)
        else:
            return sorted(array)
