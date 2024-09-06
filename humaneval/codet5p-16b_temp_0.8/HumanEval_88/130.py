
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
        return []
    if len(array) == 1:
        return array

    sorted_array = array.copy()
    sorted_array.sort()

    even_indexes = []
    odd_indexes = []

    for i in range(len(array)):
        if i % 2 == 0:
            even_indexes.append(array[i])
        else:
            odd_indexes.append(array[i])

    even_indexes.sort(reverse=True)
    odd_indexes.sort()

    result = []

    for i in range(len(array)):
        if i % 2 == 0:
            result.append(even_indexes.pop())
        else:
            result.append(odd_indexes.pop())

    return result
