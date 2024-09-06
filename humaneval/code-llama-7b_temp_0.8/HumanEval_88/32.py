
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
    def get_sum(value):
        return sum(value)

    odd_even = lambda x: x % 2 == 0 and x or x * -1

    if not array:
        return []

    if get_sum(array[0]) % 2 == 0:
        sorted_array = sorted(array, key=lambda x: odd_even(x))
    else:
        sorted_array = sorted(array, key=lambda x: odd_even(x), reverse=True)

    return sorted_array
