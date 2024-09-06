
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
    if not array:
        return []

    half_index = int(len(array) / 2)
    first_half = array[:half_index]
    second_half = array[half_index:]

    second_half.reverse()

    if sum(array[:2]) % 2 == 0:
        first_half.sort()
        second_half.sort()
    else:
        first_half.sort(reverse=True)
        second_half.sort(reverse=True)

    return first_half + second_half

