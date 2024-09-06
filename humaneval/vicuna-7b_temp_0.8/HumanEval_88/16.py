
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
    n = len(array)
    # store odd and even index values in two separate lists
    odd_index = []
    even_index = []
    for i in range(n):
        if array[i] % 2 != 0:
            odd_index.append(i)
        else:
            even_index.append(i)

    # sort the odd and even index values
    for i in odd_index:
        for j in odd_index:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    for i in even_index:
        for j in even_index:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array