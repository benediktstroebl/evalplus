
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # The solution below has O(nlogn) time complexity and O(n) space complexity.
    # The trick is to use list comprehension to create new list of tuples,
    # where each element will be a tuple of:
    # (1) the number of 1s in the binary representation of the number
    # (2) the number itself
    # This list of tuples is then sorted by the first element of the tuple,
    # and then the resulting list is returned.
    return [x for (_, x) in sorted(((bin(x).count('1'), x) for x in arr))]

