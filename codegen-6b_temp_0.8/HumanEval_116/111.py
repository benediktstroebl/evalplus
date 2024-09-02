
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
    # The key is to use nums.count(1) == nums.count(0) to identify an array of ones
    # and zeros. Then, we use the built in sorted() to sort the array. And then
    # we use the lambda to return the current number of ones as the key
    return sorted(arr, key=lambda x: (nums.count(1), x))

