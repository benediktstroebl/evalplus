
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
    length = len(array)
    if length <= 1:
        return array

    def _sort_array_helper(array, left, right):
        # This function will recursively call itself until the `left` and `right` values are the same.
        if left >= right:
            return array

        middle = (left + right) // 2
        left_array = _sort_array_helper(array, left, middle)
        right_array = _sort_array_helper(array, middle + 1, right)
        # Merge the left and right sorted arrays
        return merge(left_array, right_array)

    def merge(left_array, right_array):
        # Merges two sorted arrays
        left, right = 0, 0
        result = []
        while left < len(left_array) and right < len(right_array):
            if left_array[left] <= right_array[right]:
                result.append(left_array[left])
                left += 1
            else:
                result.append(right_array[right])
                right += 1

        # Merge any remaining elements
        result.extend(left_array[left:])
        result.extend(right_array[right:])
        return result

    return _sort_array_helper(array, 0, len(array) - 1)
