
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
    if array == [] or len(array) == 1:
        return array

    start_index = 0
    end_index = len(array) - 1

    if (array[0] + array[len(array) - 1]) % 2 == 0:
        # even numbers, descending order
        while start_index < end_index:
            if array[start_index] > array[end_index]:
                # swap values
                array[start_index], array[end_index] = array[end_index], array[start_index]

            # move to next
            start_index += 1
            end_index -= 1
    else:
        # odd numbers, ascending order
        while start_index < end_index:
            if array[start_index] < array[end_index]:
                # swap values
                array[start_index], array[end_index] = array[end_index], array[start_index]

            # move to next
            start_index += 1
            end_index -= 1

    return array

