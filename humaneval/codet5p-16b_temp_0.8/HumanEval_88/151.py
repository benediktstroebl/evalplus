
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

    if len(array) == 1:
        return array

    if len(array) == 2:
        if array[0] % 2 == 0:
            return [array[1], array[0]]
        else:
            return [array[0], array[1]]

    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]

    left_array = sort_array(left_array)
    right_array = sort_array(right_array)

    sorted_array = []

    while len(left_array) > 0 and len(right_array) > 0:
        left_first_val = left_array[0]
        right_first_val = right_array[0]

        if left_first_val + right_first_val > right_first_val + left_first_val:
            sorted_array.append(right_array.pop(0))
        else:
            sorted_array.append(left_array.pop(
