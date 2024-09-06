
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
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(array)):
        if i % 2 == 0:
            even_sum += array[i]
        else:
            odd_sum += array[i]
    if odd_sum > even_sum:
        sorted_array = sorted(array)
    elif odd_sum == even_sum:
        sorted_array = array
    else:
        sorted_array = sorted(array, reverse=True)
    return sorted_array

