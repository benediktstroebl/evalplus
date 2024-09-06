
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
    arr = sorted(arr)
    while arr:
        # Find first one greater than current median
        i = len(arr) // 2
        if arr[i] > arr[i - 1]:
            pivot = arr[i]
            j = i - 1
            for k in range(i + 1, len(arr)):
                for i in range(j + 1, len(arr)):
                    if arr[j] == pivot:
                        arr[j], arr[i] = arr[i], arr[j]
                        arr = sorted(arr)
                        break
                    elif arr[i] > arr[j]:
                        arr[j], arr[i] = arr[i], arr[j]
                        arr = sorted(arr)
                        break
                    elif arr[j] < arr[i]:
                        arr[i], arr[j] = arr[j], arr[i]
                        arr = sorted(arr)
                        break
                    else:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                if i > j:
                    break
            if i == len(arr) - 1:
                break
    return arr

test = [1, 5, 2, 3, 4]
