
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
        return array

    # for i in range(len(array)):
    #     for j in range(i, len(array)):
    #         if sum(array[i:j+1]) % 2 == 1:
    #             array[i], array[j] = array[j], array[i]
    #         else:
    #             array[i], array[j] = array[j], array[i]
    # return array

    # better code
    for i in range(1, len(array)):
        # temp = array[i]
        # if sum(array[:i]) % 2 == 1:
        #     for j in range(i, len(array)):
        #         if array[j] < array[i]:
        #             array[j], array[i] = array[i], array[j]
        #             break
        # else:
        #     for j in reversed(range(i, len(array))):
        #         if array[j] > array[i]:
        #             array[j], array[i] = array[i], array[j]
        #             break
        # array[i] = temp
        index = array[i]
        j = i - 1
        while j >= 0 and sum(array[:j + 1]) % 2 == 1:
            if array[j] < index:
                array[j], array[i] = array[i], array[j]
                break
            else:
                j -= 1
        if j == -1:
            array[i] = index

    return array


assert(sort_array([]) == [])
assert(sort_array([5]) == [5])
assert(sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5])
assert(sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0])
