
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
    length = len(array)
    if length <= 1 or length == 0:
        return array
    odd = 0
    for index in range(0, length-1):
        if odd == 1:
            temp = array[index]
            for index_j in range(length-index-1, index, -1):
                temp2 = array[index_j]
                if temp2 > temp:
                    temp = temp2
            array[index] = temp
            temp = array[length - 1 - index]
            for index_j in range(length-index-2, index, -1):
                temp2 = array[index_j]
                if temp2 > temp:
                    temp = temp2
            array[length - 1 - index] = temp
        else:
            temp = array[index]
            for index_j in range(length-index-1, index, -1):
                temp2 = array[index_j]
                if temp2 < temp:
                    temp = temp2
            array[index] = temp
            temp = array[length - 1 - index]
            for index_j in range(length-index-2, index, -1):
                temp2 = array[index_j]
                if temp2 < temp:
                    temp = temp2
            array[length - 1 - index] = temp
        odd ^= 1
    return array
