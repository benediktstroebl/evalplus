
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
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i-1] != arr[j-1]:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return arr

print(sort_array([1, 5, 2, 3, 4]))  # should return [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # should return [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # should return [0, 1, 2, 3, 4]