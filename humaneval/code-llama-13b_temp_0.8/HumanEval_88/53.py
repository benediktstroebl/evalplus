
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
    else:
        odd_sum_array = []
        even_sum_array = []
        sorted_array = []
        for index, value in enumerate(array):
            if (index + 1) % 2 != 0:
                odd_sum_array.append(value)
            else:
                even_sum_array.append(value)
        if sum(odd_sum_array) > sum(even_sum_array):
            sorted_array = sorted(even_sum_array, reverse=True)
            sorted_array += sorted(odd_sum_array)
        else:
            sorted_array = sorted(odd_sum_array)
            sorted_array += sorted(even_sum_array, reverse=True)
        return sorted_array

