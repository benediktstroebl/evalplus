
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

    # 1. Check if array is empty
    if array == []:
        return []

    # 2. For each array element, count the total of the first and last index value
    total = 0
    for i in range(len(array)):
        total += array[i]

    # 3. Return array in the appropriate order
    if (total % 2) == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
