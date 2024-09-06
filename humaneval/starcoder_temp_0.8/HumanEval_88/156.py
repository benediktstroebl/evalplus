
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

    if not length:
        return array

    left, right = 0, length - 1
    while left < right:
        if array[left] + array[right] % 2 == 0:
            array[left], array[right] = array[right], array[left]
        if array[left] + array[right] % 2 == 1:
            if array[left] % 2 == 0:
                left += 1
            else:
                array[left], array[right] = array[right], array[left]
                right -= 1

    return array

