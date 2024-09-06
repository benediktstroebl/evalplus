
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
    def _get_value(num):
        return num

    def _get_reverse_value(num):
        return -num

    def _sort(nums, ascending):
        if len(nums) < 2:
            return nums

        pivot = nums[0]

        if ascending:
            left = _sort([num for num in nums[1:] if _get_value(num) < _get_value(pivot)], ascending)
            right = _sort([num for num in nums[1:] if _get_value(num) >= _get_value(pivot)], ascending)
        else:
            left = _sort([num for num in nums[1:] if _get_reverse_value(num) < _get_reverse_value(pivot)], ascending)
            right = _sort([num for num in nums[1:] if _get_reverse_value(num) >= _get_reverse_value(pivot)], ascending)

        return left + [pivot] + right

    is_even = sum([num for num in array]) % 2 == 0
    return _sort(array, ascending=is_even)

