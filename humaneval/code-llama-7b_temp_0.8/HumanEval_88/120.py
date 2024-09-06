
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
    if n == 0 or n == 1:
        return array
    elif n == 2:
        return [min(array[0], array[1]), max(array[0], array[1])]
    elif n == 3:
        return [min(array[0], array[2]), array[1], max(array[0], array[2])]
    elif n == 4:
        return [
            min(array[0], array[3]),
            min(array[1], array[2]),
            max(array[0], array[3]),
            max(array[1], array[2]),
        ]
    odd_index_list = array[::2]
    even_index_list = array[1::2]
    if sum(odd_index_list) % 2 == 0:
        odd_index_list.sort()
        even_index_list.sort(reverse=True)
    else:
        odd_index_list.sort(reverse=True)
        even_index_list.sort()
    sorted_array = []
    for index in range(n):
        if index % 2 == 0:
            sorted_array.append(odd_index_list[index // 2])
        else:
            sorted_array.append(even_index_list[index // 2])
    return sorted_array
