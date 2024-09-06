
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
    # sort the array in descending order
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
    # check if the array is completely sorted
    if all(x == max(array) for x in array):
        return array
    else:
        # sort the first n/2 elements in descending order
        for i in range(n/2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        # sort the last n/2 elements in ascending order
        for i in range(n/2, -1, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
        return array