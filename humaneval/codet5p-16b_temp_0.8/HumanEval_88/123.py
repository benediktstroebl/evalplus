
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

    ordered_array = []
    odd_arrays = []
    even_arrays = []

    for i in array:
        if sum(i) % 2 == 0:
            even_arrays.append(i)
        else:
            odd_arrays.append(i)

    ordered_array.extend(sorted(even_arrays, reverse=True))
    ordered_array.extend(sorted(odd_arrays))

    return ordered_array
