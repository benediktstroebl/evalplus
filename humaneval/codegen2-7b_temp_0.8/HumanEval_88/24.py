
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
    def helper(array, l, r, result):
        if l >= r:
            return
        first = l
        last = r
        if array[first] + array[last] & 1:
            array[first], array[last] = array[last], array[first]
        while first + 1 < last:
            if array[first] > array[first + 1]:
                first += 1
            if array[last] > array[last - 1]:
                last -= 1
        helper(array, first, last, result)
        result.append(array[first])
        helper(array, l, last, result)
    result = []
    helper(array, 0, len(array), result)
    
