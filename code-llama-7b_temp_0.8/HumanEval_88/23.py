
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
    _array = array.copy()
    odd_even = lambda a: (a[0]+a[-1])%2 == 0
    odd_sort = lambda a: a.sort()
    even_sort = lambda a: a.sort(reverse=True)
    if len(_array) == 0:
        return []
    if len(_array) == 1:
        return _array
    if odd_even(_array):
        odd_sort(_array)
    else:
        even_sort(_array)
    return _array
