
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
    sorted_array = sorted(array)
    # first check if all elements in array are negative.
    # If so then return the sorted array
    if all(i < 0 for i in sorted_array):
        return sorted_array
    # else check if first and last element of array have odd sum
    # If so then return the sorted array
    if (sorted_array[0] + sorted_array[-1]) % 2 != 0:
        return sorted_array
    else:
        # else reverse the sorted array and return it
        return sorted_array[::-1]

