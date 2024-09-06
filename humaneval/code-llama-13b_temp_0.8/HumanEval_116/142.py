
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
    # Solution 1: O(n log n)
    # return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    # Solution 2: O(n)
    bin_arr = [bin(x)[2:] for x in arr]
    max_len = max(len(b) for b in bin_arr)
    bin_arr = [b.zfill(max_len) for b in bin_arr]
    arr.sort(key=lambda x: (bin_arr[arr.index(x)], x))
    return arr

