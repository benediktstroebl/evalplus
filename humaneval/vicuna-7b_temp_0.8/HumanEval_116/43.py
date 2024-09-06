
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
    count = {}
    for num in arr:
        count[num] = num // 2
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    binary = [str(num)[2:].zfill(3).rjust(10, '0') for num in result]
    return [int(binary[i]) for i in range(len(binary))]
