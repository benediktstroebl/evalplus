
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
    list_1 = []
    list_2 = []
    for i in range(len(array)):
        if i == 0:
            list_1.append(array[i])
        else:
            list_2.append(array[i])
    if sum(list_1)%2 == 0:
        return sorted(list_2, reverse=True)
    else:
        return sorted(list_2)
