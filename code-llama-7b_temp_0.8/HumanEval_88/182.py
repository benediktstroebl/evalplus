
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
    if array == []:
        return array

    # setup the variables
    odd = (sum(array) % 2) == 1
    even = (sum(array) % 2) == 0
    less_than = array[0]
    greater_than = array[-1]

    # if odd then sort ascending
    if odd:
        for num in array:
            if num < less_than:
                less_than = num
            if num > greater_than:
                greater_than = num
        # sort the array
        for i in range(0, len(array)):
            if array[i] < less_than:
                array[i] = less_than
                less_than = array[i]
            elif array[i] > greater_than:
                array[i] = greater_than
                greater_than = array[i]
    # if even then sort descending
    elif even:
        for num in array:
            if num > greater_than:
                greater_than = num
            if num < less_than:
                less_than = num
        # sort the array
        for i in range(0, len(array)):
            if array[i] < less_than:
                array[i] = less_than
                less_than = array[i]
            elif array[i] > greater_than:
                array[i] = greater_than
                greater_than = array[i]

    return array

