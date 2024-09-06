
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

    # divide array into two sub-arrays, one is sorted in ascending order and the other is in descending order
    a_sorted, b_sorted = [], []
    a_sum, b_sum = sum(array[:len(array) // 2]), sum(reversed(array[len(array) // 2:]))

    if a_sum % 2 == 1:
        a_sorted = sorted(array[:len(array) // 2])

    if b_sum % 2 == 0:
        b_sorted = sorted(reversed(array[len(array) // 2:]), reverse=True)

    return a_sorted + b_sorted
