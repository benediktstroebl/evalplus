
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
    array_copy = array[:]

    # need to check if array has at least one element in it
    if len(array_copy) > 0:
        first_index = array_copy[0]
        last_index = array_copy[-1]
        even_sum = first_index + last_index

        # sort array in descending order if sum of first and last element is even
        if even_sum % 2 == 0:
            array_copy.sort(reverse=True)

        # sort array in ascending order if sum of first and last element is odd
        else:
            array_copy.sort()

    return array_copy
