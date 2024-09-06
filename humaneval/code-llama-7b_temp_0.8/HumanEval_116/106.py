
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
    # -------------------------------------------------------------------------
    # O(n)
    # -------------------------------------------------------------------------
    # max_pos = 0
    # for num in arr:
    #     max_pos = max(max_pos, bin(num).count('1'))

    # result = [0] * len(arr)
    # curr = 0
    # for i in range(max_pos + 1):
    #     for num in arr:
    #         if bin(num).count('1') == i:
    #             result[curr] = num
    #             curr += 1
    # return result

    # -------------------------------------------------------------------------
    # O(n * log(n))
    # -------------------------------------------------------------------------
    # return sorted(arr, key=bin_sort_key)

