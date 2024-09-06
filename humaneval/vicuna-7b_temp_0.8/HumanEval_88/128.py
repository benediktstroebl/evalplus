
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
        return [array[0]]
    else:
        for i in range(0, n-1, 2):
            for j in range(i+1, n):
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]
        for i in range(n-1, -1, -1):
            if sum(array[i:]) % 2 == 1:
                array[i], array[i+1] = array[i+1], array[i]
            else:
                array[i], array[i+1] = array[i+1], array[i]
        return array
