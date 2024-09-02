
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
    if not arr:
        return []

    arr = [int(i) for i in arr]
    arr_len = len(arr)
    while arr_len > 1:
        # find the pivot index
        pivot_index = (arr_len - 1) // 2

        # find the pivot value
        pivot_value = arr[pivot_index]
        for i in range(pivot_index, arr_len):
            if (arr[i] > pivot_value).bit_length() > pivot_value.bit_length():
                break
        else:
            i += 1
        pivot_value_decimal = (pivot_value * 10) + (arr[i] - pivot_value) // 2

        # partition the array
        left, right = i, arr_len
        while left < right:
            # binary search
            mid = (left + right) // 2
            if (arr[mid] == pivot_value).bit_length() <= pivot_value_decimal:
                left = mid + 1
            else:
                right = mid
        arr = [i for i in arr[left:right + 1]]

    return arr[1:] + [arr[0]]
