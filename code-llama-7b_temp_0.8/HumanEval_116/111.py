
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
    zero_count = [0] * len(arr)
    one_count = [0] * len(arr)
    for i in range(len(arr)):
        zero_count[i] = get_zero_count(arr[i])
        one_count[i] = get_one_count(arr[i])

    zero_count.sort(key=lambda x: x)
    one_count.sort(key=lambda x: x)

    result = [0] * len(arr)
    index_one_count = 0
    index_zero_count = 0

    for i in range(len(arr)):
        if zero_count[index_zero_count] < one_count[index_one_count]:
            result[i] = arr[zero_count[index_zero_count]]
            index_zero_count += 1
        else:
            result[i] = arr[one_count[index_one_count]]
            index_one_count += 1

    return result

