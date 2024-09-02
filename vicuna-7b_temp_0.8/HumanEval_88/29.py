
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

    # Check if the array is empty or not
    if len(array) == 0:
        return []

    # Initialize two variables, first_sum and second_sum, to keep track of the sum of first and second half of the array
    first_sum = 0
    second_sum = 0
    last_index = len(array) - 1

    # Loop through the array and check the sum
    for i in range(0, len(array)):
        if i == 0 or i == last_index:
            first_sum += array[i]
        else:
            second_sum += array[i]

    # Determine the direction of the sort
    odd_sum = first_sum % 2

    if odd_sum == 0:
        direction = 1
    else:
        direction = -1

    sorted_array = array[:]

    # Sort the array in the direction determined above
    for i in range(0, len(array)):
        index = (i + direction) % len(array)
        sorted_array[index] = array[i]

    return sorted_array