
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
    l = len(array)
    if l == 0:
        return array
    if l == 1:
        return array
    middle = l // 2
    pivot = array[middle]
    left = [x for x in array[:middle]]
    right = [x for x in array[middle + 1:]]
    return left + sort_array([x for x in pivot if x >= pivot[0] if x <= pivot[-1]]) + right + sort_array([x for x in pivot if x < pivot[0] if x >= pivot[-1
