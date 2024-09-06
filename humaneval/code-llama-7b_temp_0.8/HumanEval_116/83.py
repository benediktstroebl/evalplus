
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
    result = []
    for i in arr:
        binary = bin(i)
        if binary.count('1') not in result:
            result.append([])
            result[-1].append(i)
            continue
        else:
            index = result.index([item for item in result if item.count('1') == binary.count('1')][0])
            result[index].append(i)

    return [item for sublist in result for item in sorted(sublist)]
