
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
    if not array:
        return []

    def partition(array, low, high):
        while True:
            while low < high and array[low] <= array[low + 1]:
                low += 1
            while low < high and array[high] >= array[high - 1]:
                high -= 1
            if low >= high:
                return low
            array[low], array[high] = array[high], array[low]

    def sort(array, low, high):
        if low >= high:
            return
        p = partition(array, low, high)
        sort(array, low, p)
        sort(array, p + 1, high)

    n = len(array)
    sort(array, 0, n - 1)
    return array
