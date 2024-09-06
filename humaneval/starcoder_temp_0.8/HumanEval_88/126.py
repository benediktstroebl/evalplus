
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

    def swap(array, i, j):
        array[i], array[j] = array[j], array[i]

    def partition(array, start, end):
        pivot = array[(start + end) // 2]
        while start < end:
            while array[start] < pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            if start < end:
                swap(array, start, end)
        return end

    def quick_sort(array, start, end):
        if start < end:
            partition_index = partition(array, start, end)
            quick_sort(array, start, partition_index)
            quick_sort(array, partition_index + 1, end)

    quick_sort(array, 0, len(array) - 1)
    return array

