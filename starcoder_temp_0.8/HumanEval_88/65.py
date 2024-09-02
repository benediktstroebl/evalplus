
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

    def sort(array, low, high):
        if high <= low:
            return

        mid = (high + low) // 2
        sort(array, low, mid)
        sort(array, mid + 1, high)

        if array[mid] > array[high]:
            array[mid], array[high] = array[high], array[mid]

        if array[mid] > array[low]:
            array[mid], array[low] = array[low], array[mid]

        sort(array, low, high - 1)

    sort(array, 0, len(array) - 1)
    return array
