
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
    sorted_array = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] % 2 == 0:
                sorted_array.append(array[j])
                sorted_array.append(array[i])
                break
            if array[i] + array[j] % 2 == 1:
                sorted_array.append(array[i])
                sorted_array.append(array[j])
                break
    return sorted_array

