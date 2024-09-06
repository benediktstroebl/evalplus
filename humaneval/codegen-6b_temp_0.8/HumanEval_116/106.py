
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
    # max_num_of_ones = 0
    # max_index = 0
    # for i in range(len(arr)):
    #     number_of_ones = bin(arr[i]).count('1')
    #     if number_of_ones > max_num_of_ones:
    #         max_num_of_ones = number_of_ones
    #         max_index = i
    # arr[max_index] = 0
    # return arr

    number_of_ones = []
    for i in range(len(arr)):
        number_of_ones.append((bin(arr[i]).count('1'), arr[i]))
    number_of_ones.sort()
    result = []
    for i in range(len(arr)):
        result.append(number_of_ones[i][1])
    return result
