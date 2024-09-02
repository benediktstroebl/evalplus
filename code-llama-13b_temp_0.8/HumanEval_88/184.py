
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

    if len(array) == 1:
        return [array[0]]

    # starts = [0]
    # ends = [-1]
    starts = []
    ends = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            starts.append(i)
        else:
            ends.append(i)

    # print(starts)
    # print(ends)

    starts.reverse()
    sorted_array = []
    while starts or ends:
        if not starts:
            sorted_array.append(array[ends.pop()])
        elif not ends:
            sorted_array.append(array[starts.pop()])
        elif starts[-1] < ends[-1]:
            sorted_array.append(array[starts.pop()])
        else:
            sorted_array.append(array[ends.pop()])

    return sorted_array

