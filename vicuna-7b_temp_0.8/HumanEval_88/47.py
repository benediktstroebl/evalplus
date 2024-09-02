
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
    # Create a new list to store the sorted array
    new_list = []
    # Iterate through the original list
    for element in array:
        # Check the sum of the first and last element in the sub-list
        first_last = (element[0], element[-1])
        # If the sum is odd, we add the element to the new list and then sort the sub-list
        if sum(first_last) % 2 == 1:
            new_list.append(element)
            # Sort the sub-list in ascending order
            new_list.sort()
        # If the sum is even, we add the element to the new list and then sort the sub-list in descending order
        else:
            new_list.append(element)
            new_list.sort(reverse=True)
    # Return the sorted new list
    return new_list