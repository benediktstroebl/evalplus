
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
    
    copy_array = list(array)
    first = 0
    last = len(array) - 1
    
    while first < last:
        if sum(copy_array[first], copy_array[last]) % 2 == 0:
            copy_array[first], copy_array[last] = copy_array[last], copy_array[first]
            first += 1
            last -= 1
        elif sum(copy_array[first], copy_array[last]) % 2 == 1:
            if copy_array[first] < copy_array[last]:
                first += 1
            else:
                copy_array[first], copy_array[last] = copy_array[last], copy_array[first]
                first += 1
                last -= 1
    
    return copy_array
