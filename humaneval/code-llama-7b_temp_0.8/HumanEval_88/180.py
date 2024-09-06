
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
    # get the last index
    last = len(array) - 1

    # get the first and last value
    first_value = array[0]
    last_value = array[last]

    # calculate the total sum
    total_sum = first_value + last_value

    # if odd number, sort in ascending order
    if total_sum & 1:
        return sorted(array)

    # if even number, sort in descending order
    return sorted(array, reverse=True)

