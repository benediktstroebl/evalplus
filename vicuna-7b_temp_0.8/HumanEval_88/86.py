
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
    def sum_odd_or_even(array):
        end = len(array)
        count = 0
        while end > 0:
            odd_sum = array[end - 1] + array[end - 2] + ... + array[1]
            count += odd_sum % 2
            array[end - 1] = array[0]
            array.pop(0)
            end = end - 2
            odd_sum = 2 * odd_sum // 2
        return count

    return sum_odd_or_even(array)