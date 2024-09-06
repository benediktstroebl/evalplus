
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

    # iterate the given array until the last element
    for i in range(len(array) - 1):

        # iterate the given array until the end, check the
        # 1st element is bigger than the last element
        for j in range(i, len(array)):

            # if the 1st element is bigger than the last element
            # swap them
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    # if the sum( first index value, last index value) is odd
    # sort the given array in ascending order
    if array[0] + array[-1] % 2:
        return sorted(array)

    # if the sum( first index value, last index value) is even
    # sort the given array in descending order
    else:
        return sorted(array, reverse=True)
