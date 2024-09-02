
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
        return [0] * n
    s = sum(array)
    if s % 2 == 0:
        return sorted(array, reverse=True)
    else:
        s1 = sum(array[:-1])
        s2 = sum(array[1:])
        if s1 % 2 == 0 and s2 % 2 == 0:
            return sorted(array, reverse=True)
        elif s1 % 2 == 1 and s2 % 2 == 0:
            return [0] + list(array)
        else:
            return list(array)
