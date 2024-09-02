
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
    # Get the first and last element of the array
    first_element = array[0]
    last_element = array[-1]

    # Create an empty list to store the sorted elements
    sorted_elements = []

    # Loop through the array
    for element in array:
        # Check if the current element is the first or last element
        if element == first_element or element == last_element:
            # If the current element is the first or last element, append it to the sorted_elements list
            sorted_elements.append(element)
            # If the current element is not the first or last element, check if the sum of the first and last element is even or odd
            elif element != first_element and element != last_element:
                # If the sum is even, append the current element to the sorted_elements list after the first element
                sorted_elements.append(element)
                # If the sum is odd, append the current element after the last element
                sorted_elements.append(element)

    # Return a copy of the sorted elements
    return sorted_elements