
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

    # Creating a copy of the array
    array = list(array)

    # Creating a new empty list to store the sorted elements
    sorted_array = []

    # Iterating through the elements of the original array
    for element in array:

        # Creating a new empty list to store the remaining elements
        remaining_array = []

        # Iterating through the remaining elements of the original array
        for remaining_element in array:

            # If the first and last elements of the remaining sub-array are equal,
            # then they don't affect the sum of the sub-array, so we can ignore them
            if remaining_element == remaining_array[-1]:
                remaining_array.append(remaining_element)
                remaining_array.append(remaining_array.pop())
                # If the sum of the remaining sub-array is odd, then we sort the sub-array
                # in ascending order
                elif sum(remaining_array) % 2 == 1:
                    sorted_array.append(remaining_array[::-1])
                    # If the sum of the remaining sub-array is even, then we sort the sub-array
                    # in descending order
                elif sum(remaining_array) % 2 == 0:
                    sorted_array.append(remaining_array[::])
                    # If the remaining sub-array is empty, then we add the element to the sorted_array
                    if remaining_array == []:
                        sorted_array.append(remaining_element)

        # Adding the current element and its remaining sub-array to the sorted_array
        sorted_array.append(element)
        sorted_array.extend(remaining_array)

    return sorted_array