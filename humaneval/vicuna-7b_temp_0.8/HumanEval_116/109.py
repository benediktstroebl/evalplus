
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
    n = len(arr)
    #helper function to count the number of 1's in binary representation
    def count_ones(x):
        return sum([1 for i in range(len(str(x))) if str(x)[:i] == '1'])

    #sort based on the number of ones
    arr = sorted(arr, key=count_ones)
    #sort based on decimal value when the number of ones is same
    return arr[arr.count(arr[0])]