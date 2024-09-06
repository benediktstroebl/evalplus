
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
    if length <= 1:
        return array
    
    mid = length // 2
    
    left = sort_array(array[:mid])
    right = sort_array(array[mid:])
    
    sorted_array = []
    
    while len(left) > 0 and len(right) > 0:
        if left[0] + right[0] > right[0] + left[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    
    sorted_array += left
    sorted_array += right
    
    return sorted_array
    
    
