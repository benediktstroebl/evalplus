
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
    bin_arr = ["".join(str(bin(i)[2:])) for i in arr]
    count_arr = [sum([int(i) for i in k]) for k in bin_arr]
    # print(count_arr)
    sorted_arr = [i[0] for i in sorted(zip(arr, count_arr), key=lambda x: (x[1], x[0]), reverse=False)]
    # print(sorted_arr)
    return sorted_arr

