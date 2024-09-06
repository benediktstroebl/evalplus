
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

    l = len(array)
    if l == 1:
        return array

    if l % 2 == 1:
        i = 0
        while i < l:
            if i == l - 1:
                break

            if array[i] % 2 == 1:
                temp = array[i]
                array[i] = array[l - 1]
                array[l - 1] = temp
                break
            i += 1
    else:
        i = 0
        while i < l:
            if i == l - 1:
                break

            if array[i] % 2 == 0:
                temp = array[i]
                array[i] = array[l - 1]
                array[l - 1] = temp
                break
            i += 1

    return array
