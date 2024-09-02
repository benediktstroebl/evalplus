
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
    if n == 0:
        return []
    else:
        pivot = arr[0]
        left_ptr = 0
        right_ptr = 0
        while right_ptr < n:
            while left_ptr < n and arr[left_ptr] < pivot:
                left_ptr += 1
            while right_ptr < n and arr[right_ptr] > pivot:
                right_ptr += 1
            if left_ptr == n:
                break
            if right_ptr == n:
                break
            # swap arr[left_ptr] with arr[right_ptr]
            arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]
            # move left_ptr and right_ptr
            left_ptr += 1
            arr[right_ptr] = arr[left_ptr]
            right_ptr += 1

    return arr