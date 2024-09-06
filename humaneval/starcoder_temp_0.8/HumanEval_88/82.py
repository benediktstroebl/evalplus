
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
    # max_val = max(array)
    # sum_val = sum(array)
    # if sum_val % 2 == 0:
    #     return sorted(array, reverse=True)
    # else:
    #     return sorted(array, reverse=False)

    # max_index = array.index(max_val)
    # min_index = array.index(max(array[0:max_index]))
    # if sum(array[min_index:max_index]) % 2 == 0:
    #     return sorted(array[min_index:max_index])
    # else:
    #     return sorted(array[min_index:max_index], reverse=True)

    # max_index = array.index(max_val)
    # first_half = array[0:max_index+1]
    # second_half = array[max_index+1:]
    # first_half.sort()
    # second_half.sort(reverse=True)
    # return first_half + second_half

    min_val = min(array)
    max_val = max(array)
    if sum(array) % 2 == 0:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
