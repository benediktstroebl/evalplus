
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
    l = len(arr)

    idx = {'bits': [], 'values': []}
    for i in range(l):
        bit = bin(arr[i])[2:]
        if bit.count('1') > bit.count('0'):
            idx['bits'].append(bit)
            idx['values'].append(arr[i])

    idx['bits'].sort()
    idx['values'].sort()

    return [idx['values'][i] for i in range(l)]

