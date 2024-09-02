
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
    # set the sum as the variable for the array to sort
    sum = array[0] + array[len(array) - 1]
    sorted_array = []

    if sum % 2 == 0:
        for value in array:
            sorted_array.append(value)
        sorted_array.sort(reverse=True)
        return sorted_array

    else:
        for value in array:
            sorted_array.append(value)
        sorted_array.sort()
        return sorted_array


    return sorted_array


    """
    # The following method was used to try and sort an array using .sort() and .reverse().
    # It did not work and was not ideal.
    sum = array[0] + array[len(array) - 1]
    sorted_array = []

    if sum % 2 == 0:
        for value in array:
            sorted_array.append(value)
        sorted_array.sort(reverse=False)
        return sorted_array

    else:
        for value in array:
            sorted_array.append(value)
        sorted_array.sort(reverse=True)
        return sorted_array

    return sorted_array
    """
