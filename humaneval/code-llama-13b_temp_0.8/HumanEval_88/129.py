
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
    if len(array) == 0:
        return array

    def is_even(first_value, last_value):
        return (first_value + last_value) % 2 == 0

    start = 0
    end = len(array) - 1
    while start < end:
        while start < len(array) and is_even(array[start], array[end]):
            start += 1
        while end >= 0 and is_even(array[start], array[end]):
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]
    return array

