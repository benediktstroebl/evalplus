
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
    bits = []
    for i in arr:
        bits.append(i.bit_length())

    sorted_bits = sorted(list(set(bits)))

    new_arr = []
    for bit in sorted_bits:
        temp_arr = [x for x in arr if x.bit_length() == bit]
        temp_arr.sort()
        new_arr.extend(temp_arr)

    return new_arr

