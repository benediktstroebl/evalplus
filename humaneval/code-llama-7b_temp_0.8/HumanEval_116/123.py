
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
    ones_count = [0] * 32

    for num in arr:
        if num < 0:
            raise ValueError("Negative number is not allowed")

        i = 0
        while num > 0:
            if num & 1 == 1:
                ones_count[i] += 1
            num >>= 1
            i += 1

    nums_with_ones_count = [0] * len(arr)
    for i, count in enumerate(ones_count):
        nums_with_ones_count[count] = (nums_with_ones_count[count] * 10) + i

    for i, _ in enumerate(nums_with_ones_count):
        if nums_with_ones_count[i] == 0:
            nums_with_ones_count[i] = -1

    return sorted(arr, key=lambda x: nums_with_ones_count[x])
