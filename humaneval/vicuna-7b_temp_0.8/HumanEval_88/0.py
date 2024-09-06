
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
    # check if the array is empty
    if not array:
        return []

    # set the sum to 0
    sum = 0

    # sort the array in ascending order
    sorted_array = sorted(array, reverse=True)

    # sort the array again to correct the order
    for i in range(len(sorted_array)):
        for j in range(i, len(sorted_array)):
            if (sorted_array[j] - sorted_array[i]) % 2 == 0:
                sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]
                break

    # print the sorted array
    return [x for x in sorted_array]