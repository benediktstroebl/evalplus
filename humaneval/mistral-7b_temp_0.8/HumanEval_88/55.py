
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
    # Takes an integer array and sorts it in ascending order if the sum of the first and last indexes is
    # odd, or sorts it in descending order if the sum is even. Returns the sorted array.

    # 1st approach:
    # Sort the array
    # Find the sum of the first and last indexes
    # If the sum is even, sort the array in descending order
    # If the sum is odd, sort the array in ascending order
    # Return the sorted array

    sorted_array = sorted(array)
    first_index = 0
    last_index = len(array) - 1
    sum = array[first_index] + array[last_index]
    if sum % 2 == 0:
        sorted_array.reverse()
    return sorted_array

