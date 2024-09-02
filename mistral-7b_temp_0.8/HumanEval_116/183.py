
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
    arr_sorted = []
    for elem in arr:
        if elem > 0:
            temp = bin(elem)
            temp = temp[2:]
            temp = list(temp)
            temp.sort(reverse=True)
            arr_sorted.append(int(''.join(temp)))
        else:
            arr_sorted.append(elem)
    arr_sorted.sort()
    return arr_sorted
