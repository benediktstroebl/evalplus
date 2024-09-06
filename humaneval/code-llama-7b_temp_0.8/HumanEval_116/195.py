
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
    bits_array = []
    for number in arr:
        bits = str(bin(number))[2:]
        if number == 0:
            bits = "00000000000000000000000000000000"
        elif number > 0:
            bits = bits.zfill(32)
        else:
            bits = bits.zfill(32)
        bits_array.append([bits.count("1"), bits])

    sorted_bits_array = sorted(bits_array, key=lambda x: (x[0], x[1]))
    return [int(number, 2) for number in [number[1] for number in sorted_bits_array]]

