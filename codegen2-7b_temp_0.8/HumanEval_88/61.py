
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
    def partition(array, first, last):
        pivot = array[first]
        while first < last:
            while first < last and array[last] >= pivot:
                last -= 1
            array[first] = array[last]
            while first < last and array[first] <= pivot:
                first += 1
            array[last] = array[first]
        array[first] = pivot
        return first

    def sort_array_helper(array, first, last):
        if last - first == 1:
            return
        pivot = partition(array, first, last)
        sort_array_helper(array, first, pivot - 1)
        sort_array_helper(array, pivot + 1, last)

    sort_array_helper(array, 0, len(array))
