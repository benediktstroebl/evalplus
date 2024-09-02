from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # NOTE: This implementation requires the values to be in order:
    # 0,1,2,3,4,5,6,7,8,9
    # Also, the values are stored in the list in the order 0,3,1,5
    # NOTE: This implementation requires that the values are ordered, but the order is not required to be the
    # order in which they appear in the list.

    numbers_list = numbers.split()
    # print(numbers_list)
    numbers_sorted_list = []
    for i in range(len(numbers_list)):
        if numbers_list[i] == "one":
            numbers_sorted_list.append(1)
        elif numbers_list[i] == "two":
            numbers_sorted_list.append(2)
        elif numbers_list[i] == "three":
            numbers_sorted_list.append(3)
        elif numbers_list[i] == "four":
            numbers_sorted_list.append(4)
        elif numbers_list[i] == "five
