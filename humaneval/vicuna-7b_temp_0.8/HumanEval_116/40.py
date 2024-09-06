
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
    left, right = 1 << len(arr) - 1, 0
    while left >= right:
        # binary search
        mid = (left + right) // 2
        if arr[mid] == 1:
            # if middle element is 1, we know the array is sorted
            return [arr[i] for i in range(len(arr)) if arr[i] == 1]
        elif mid > arr[mid - 1]:
            # if middle element is smaller than the element on the left of it,
            # we know the array is sorted
            return [arr[i] for i in range(len(arr)) if arr[i] == 1]
        else:
            # if middle element is greater than the element on the right of it,
            # we know the array is sorted
            return [arr[i] for i in range(len(arr)) if arr[i] == 1]
    # if we reach this point, the middle element is 0 and we don't know the
    # order, so return an empty list
    return []
