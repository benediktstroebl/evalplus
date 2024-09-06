
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

    left = 0
    right = length - 1
    current = left

    while current <= right:
        if array[current] % 2 == 0:
            current += 1
        else:
            if array[current] % 2!= 0 and array[left] % 2!= 0:
                array[left], array[current] = array[current], array[left]
                left += 1
                current = left
            elif array[current] % 2!= 0 and array[right] % 2!= 0:
                array[right], array[current] = array[current], array[right]
                right -= 1
            else:
                current += 1

    return array
