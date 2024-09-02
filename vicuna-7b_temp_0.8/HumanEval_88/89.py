
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
    if n == 0:
        return []
    mid = n // 2
    if n % 2 == 0:
        if sum(map(int, array)) % 2 == 0:
            array = sorted(array)
        else:
            array = [a + b for a, b in zip(array[::-1], array)]
            array.reverse()
    else:
        if sum(map(int, array)) % 2 == 1:
            array = [a + b for a, b in zip(array[::-1], array)]
            array.reverse()
        else:
            array = [a + b for a, b in zip(array, reversed(array))]
            array.reverse()
    return array