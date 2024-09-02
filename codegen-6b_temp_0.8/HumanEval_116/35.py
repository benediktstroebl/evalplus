
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
    zero_ones, no_zero_ones = {}, {}
    for value in arr:
        binary_value = bin(value)[2:]
        bits = len(binary_value)
        if bits % 2 == 0:
            zero_ones[value] = bits
        else:
            no_zero_ones[value] = bits
    sorted_zero_ones = sorted(zero_ones.items(), key=itemgetter(1))
    sorted_no_zero_ones = sorted(no_zero_ones.items(), key=itemgetter(1))
    return [value for value, _ in sorted_zero_ones] + [value for value, _ in sorted_no_zero_ones]

