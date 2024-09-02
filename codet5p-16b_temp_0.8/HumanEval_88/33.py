
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

    result = []

    while len(array) > 0:
        current_min = array[0]
        current_max = array[0]
        for value in array:
            if value > current_max:
                current_max = value
            elif value < current_min:
                current_min = value

        if (current_min + current_max) % 2 == 0:
            result.append(current_max)
            array.remove(current_max)
        else:
            result.append(current_min)
            array.remove(current_min)

    return result
