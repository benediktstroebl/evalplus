
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

    left_index = 0
    right_index = len(array) - 1
    sorted_array = [array[0]]
    
    while left_index < right_index:
        current_sum = array[left_index] + array[right_index]
        if current_sum % 2 == 0:
            sorted_array.append(array[right_index])
            right_index -= 1
        else:
            sorted_array.append(array[left_index])
            left_index += 1
    
    if left_index == right_index:
        sorted_array.append(array[left_index])
    else:
        sorted_array.append(array[right_index])

    return sorted_array


