
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
    ret = {
        "ones": [arr[i] for i in range(n) if (sum(int(j) for j in format(arr[i], 'b')) == 1)],
        "zeros": [arr[i] for i in range(n) if (sum(int(j) for j in format(arr[i], 'b')) == 0)]
    }
    return [x for x in sorted(ret.values())]

