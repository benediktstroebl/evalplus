
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
    n = len(array)
    # if the array is empty or has only one element, return the input array.
    if n == 0 or n == 1:
        return array
    # create a new array to store the sorted array.
    # use a dictionary to store the sum of values in the given array,
    # with the key as the index and the value as the sum.
    sums = {}
    # iterate through the given array.
    for i in range(n):
        # sum the values in the given array.
        sum = array[i] + array[i]
        # check if the sum is odd or even.
        if sum % 2 == 0:
            # if the sum is even, the sorted array is already in the given array.
            return array
        # if the sum is odd, add the current value to the sums dictionary.
        sums[i] = sum
    # sort the given array.
    sorted_array = sorted(array)
    # sort the sums dictionary.
    sorted_sums = sorted(sums.items())
    # iterate through the sorted array and sums dictionary.
    for i in range(n):
        # get the current value and its corresponding sum from the sorted_array and sorted_sums.
        value = sorted_array[i]
        sum = sorted_sums[i]
        # update the value in the input array to the current value.
        array[i] = value
    # return a copy of the input array.
    return array