
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

    # The trick here is that we don't actually need to sort the array. We can find the correct sorted order
    # at the same time we find the correct sorted order of the initial array, and then we use the correct
    # ordering to re-order the initial array in place.
    #
    # It should be noted that this is not a particularly memory efficient solution (I suppose you could
    # reduce the memory usage of this by not creating the temp array and working directly with the
    # original array), but it's also a solution that should be pretty fast because it is a very simple
    # algorithm.

    if array == []:
        return []

    if len(array) == 1:
        return array

    # The first step is to determine if the array should be sorted ascending or descending.
    #
    # We do this by checking if the sum of the first and last values in the array is odd or even.
    # If the sum is odd, then we want to sort in ascending order, otherwise we want to sort in descending order.

    sum_first_last = array[0] + array[-1]

    if sum_first_last % 2 == 0:
        sorted_order = True
    else:
        sorted_order = False

    # Create a temporary array to store the correct sorted order of the input array.

    temp_array = [0] * len(array)

    # Next, we want to find the correct sorted order of the input array.

    # For ascending order, we start with the minimum value in the array and add it to the temp array.

    if sorted_order:
        current_val = array[0]
        index = 0

        while index < len(array):
            temp_array[index] = current_val
            index += 1

            if index < len(array):
                current_val += 1

    # For descending order, we start with the maximum value in the array and add it to the temp array.

    else:
        current_val = array[-1]
        index = 0

        while index < len(array):
            temp_array[index] = current
