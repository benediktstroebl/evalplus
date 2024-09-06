
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

    if len(array) <= 1:
        return array
    pivot = 0
    for i in range(1, len(array)):
        if array[i] < array[pivot]:
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1
    array[pivot], array[0] = array[0], array[pivot]
    left, right = [], []
    for i in range(1, len(array)):
        if i % 2 == 0:
            if array[i] > array[pivot]:
                left.append(array[i])
            else:
                right.append(array[i])
        else:
            if array[i] > array[pivot]:
                right.append(array[i])
            else:
                left.append(array[i])
    return sort_array(left) + [array[pivot]] + sort_array(right)
