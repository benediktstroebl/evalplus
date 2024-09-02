
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
    zero_count = arr.count(0)
    one_count = arr.count(1)
    two_count = arr.count(2)
    three_count = arr.count(3)
    four_count = arr.count(4)
    five_count = arr.count(5)
    six_count = arr.count(6)
    seven_count = arr.count(7)
    eight_count = arr.count(8)
    nine_count = arr.count(9)
    ones_list = [1] * one_count
    twos_list = [2] * two_count
    threes_list = [3] * three_count
    fours_list = [4] * four_count
    fives_list = [5] * five_count
    sixes_list = [6] * six_count
    sevens_list = [7] * seven_count
    eights_list = [8] * eight_count
    nines_list = [9] * nine_count
    zeroes_list = [0] * zero_count
    all_count = ones_list + twos_list + threes_list + fours_list + fives_list + sixes_list + sevens_list + eights_list + nines_list + zeroes_list
    return all_count
