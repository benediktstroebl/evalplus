
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

    # Create an empty list for the sorted array
    sorted_array = []

    # Calculate the sum of the first and last elements
    sum_of_first_and_last = array[0] + array[-1]

    # Sort the array in ascending order if the sum is odd
    if sum_of_first_and_last % 2 != 0:
        sorted_array = sorted(array)

    # Sort the array in descending order if the sum is even
    elif sum_of_first_and_last % 2 == 0:
        sorted_array = sorted(array, reverse=True)

    # Return the sorted array
    return sorted_array
