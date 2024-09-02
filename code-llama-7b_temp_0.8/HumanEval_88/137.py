
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

    result = array[:]
    if len(result) == 0:
        return []

    odd_even = (sum(result[0:2])) % 2 == 0
    print(odd_even)

    def sort_ascending(sub_list):
        print(sub_list)
        sub_list.sort()
        print(sub_list)
        return sub_list

    def sort_descending(sub_list):
        sub_list.reverse()
        return sub_list

    if odd_even:
        result[0:2] = sort_ascending(result[0:2])
        result[2:] = sort_descending(result[2:])
    else:
        result[0:2] = sort_descending(result[0:2])
        result[2:] = sort_ascending(result[2:])
    return result

