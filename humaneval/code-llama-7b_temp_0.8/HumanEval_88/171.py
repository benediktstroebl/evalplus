
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
    # Check the list is empty or not
    if len(array) == 0:
        return []
    # Initialize variables
    odd = 0
    odd_array = []
    even_array = []
    # Loop through array
    for idx, value in enumerate(array):
        if idx == 0 or idx == (len(array) - 1):
            odd += value
        if value < array[0]:
            odd_array.append(value)
        else:
            even_array.append(value)
    # Check if the sum of array is odd or even
    if odd % 2 == 0:
        even_array.sort()
        return even_array + odd_array
    else:
        odd_array.sort()
        return odd_array + even_array

