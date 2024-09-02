
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
    odd_even_sort = 1 if sum(array[:2]) % 2 == 1 else -1

    # Make a copy of the original array.
    sorted_array = [x for x in array]

    # Move all values from the original array to the new sorted array.
    for idx in range(len(array)):
        value = array[idx]
        sorted_idx = idx + 1
        while sorted_idx < len(sorted_array) and value < sorted_array[sorted_idx]:
            sorted_array[sorted_idx - 1] = sorted_array[sorted_idx]
            sorted_idx += 1
        sorted_array[sorted_idx - 1] = value

    if odd_even_sort == -1:
        sorted_array.reverse()

    return sorted_array
