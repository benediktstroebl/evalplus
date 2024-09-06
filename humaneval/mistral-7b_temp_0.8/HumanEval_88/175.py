
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

    def sum_first_and_last_index(array):
        sum = 0
        if len(array) == 0:
            return sum
        sum += array[0]
        sum += array[-1]
        return sum

    def sort_array_in_ascending_order(array):
        return sorted(array)

    def sort_array_in_descending_order(array):
        return sorted(array, reverse=True)

    array_sum = sum_first_and_last_index(array)
    if array_sum % 2 == 0:
        return sort_array_in_descending_order(array)
    return sort_array_in_ascending_order(array)

