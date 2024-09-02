
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

    # --- bubble sort implementation ---
    # for i in range(len(arr) - 1):
    #     for j in range(i, len(arr)):
    #         if binary_count(arr[i]) > binary_count(arr[j]):
    #             arr[i], arr[j] = arr[j], arr[i]
    # return arr

    # --- merge sort implementation ---
    # def merge(left, right):
    #     merged = []
    #     while left and right:
    #         if binary_count(left[0]) < binary_count(right[0]):
    #             merged.append(left.pop(0))
    #         else:
    #             merged.append(right.pop(0))
    #     merged.extend(left)
    #     merged.extend(right)
    #     return merged

    # if len(arr) > 1:
    #     middle = len(arr) // 2
    #     left = arr[:middle]
    #     right = arr[middle:]
    #     return merge(sort_array(left), sort_array(right))
    # else:
    #     return arr

    # --- quick sort implementation ---
    return quicksort(arr)

