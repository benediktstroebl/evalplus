
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

    for i in range(len(arr)):
        num_ones = bin(arr[i]).count("1")
        # print("num_ones", num_ones)
        if num_ones not in sorted_list:
            sorted_list.append(num_ones)

    # print(sorted_list)

    sorted_list.sort()
    # print(sorted_list)

    sorted_list_2 = []
    for i in sorted_list:
        sorted_list_2 += [a for a in arr if bin(a).count("1") == i]

    return sorted_list_2

