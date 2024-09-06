
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

    n = len(array)
    #helper function
    def helper(i, j, k):
        if i == j:
            return array[i]
        elif array[i] < array[j]:
            helper(i+1, j, k+1)
        elif array[i] > array[j]:
            helper(i+1, j, k+1)
        else:
            helper(i+1, j, k)
    
    #sorting
    for i in range(n-1):
        k = (n-i-1)/2
        helper(i, k, 0)

    #sorting the odd and even sum
    if n % 2 == 0:
        k = (n-1) / 2
        for i in range(k, n):
            array[i], array[k] = array[k], array[i]
    else:
        k = (n-1) / 2
        for i in range(k, n):
            array[i], array[k] = array[k], array[i]

    return array