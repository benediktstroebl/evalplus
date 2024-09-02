
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
    # Find the Sum
    first_index_value = array[0]
    last_index_value = array[-1]
    sum_of_first_and_last_index_value = first_index_value + last_index_value

    # Create a copy of the given array
    sorted_array = []
    for i in range(0, len(array)):
        sorted_array.append(array[i])

    # Create a new variable and set it to the sum of the first and last index value
    # Divide the sum into three parts, if the sum is odd, divide the sum by 3 and make it an integer
    # If the sum is even, divide the sum by 2 and make it an integer
    # Set a new variable to that value
    new_variable = sum_of_first_and_last_index_value
    new_variable = int(new_variable / 2)

    # Sort the array
    if sum_of_first_and_last_index_value % 2 == 1:
        sorted_array.sort()
    elif sum_of_first_and_last_index_value % 2 == 0:
        sorted_array.sort(reverse=True)

    return sorted_array
