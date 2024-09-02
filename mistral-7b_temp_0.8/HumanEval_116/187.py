
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
    sorted_list = []
    for i in arr:
        binary_list = []
        while i > 0:
            binary_list.append(i % 2)
            i = int(i / 2)
        sorted_list.append(binary_list)
    sorted_list.sort(key=lambda x: x.count(1))
    sorted_list.sort(key=lambda x: sum(x))
    return [int("".join(map(str, x)), 2) for x in sorted_list]
