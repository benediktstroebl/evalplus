
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

    def get_even_sum(array):
        return array[0] + array[-1]

    def sort_even(array):
        return array[::-1]

    def sort_odd(array):
        return array

    array_length = len(array)

    if array_length == 0 or array_length == 1:
        return array

    if array_length == 2:
        if array[0] == array[1]:
            return array
        else:
            if get_even_sum(array) % 2 == 0:
                return sort_even(array)
            else:
                return sort_odd(array)

    mid = array_length // 2

    left = array[:mid]
    right = array[mid:]

    if get_even_sum(left) % 2 == 0:
        left = sort_even(left)
    else:
        left = sort_odd(left)

    if get_even_sum(right) % 2 == 0:
        right
