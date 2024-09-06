
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
    if n == 0:
        return []
    elif n == 1:
        return array[0]
    else:
        # sort the array in ascending order
        array.sort()
        # find the first odd number
        i = 0
        while i < n-1 and not (array[i] + array[i+1]) % 2 == 0:
            i += 1
        # if there is an odd number,
        # return the array in descending order based on the first and last number
        if i < n-1:
            return array[i] + list(range(i+1, n)) + array[i+1:]
        # if there is no odd number,
        # return the array in ascending order
        else:
            return array
