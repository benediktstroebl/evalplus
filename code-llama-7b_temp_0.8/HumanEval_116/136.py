
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
    number_of_ones_dict = {}
    for i in range(len(arr)):
        number_of_ones = count_number_of_ones(arr[i])
        if number_of_ones not in number_of_ones_dict:
            number_of_ones_dict[number_of_ones] = [arr[i]]
        else:
            number_of_ones_dict[number_of_ones].append(arr[i])
    return sum(number_of_ones_dict.values(), [])

