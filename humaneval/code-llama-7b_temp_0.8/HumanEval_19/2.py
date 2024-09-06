from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if not numbers:
        return numbers

    zero_one_two = 'zero one two'
    three_four_five = 'three four five'
    six_seven_eight = 'six seven eight'
    nine = 'nine'
    new_num = ''

    for number in numbers.split():
        if number in zero_one_two:
            new_num += zero_one_two[zero_one_two.index(number) : zero_one_two.index(number) + 1] + ' '
        elif number in three_four_five:
            new_num += three_four_five[three_four_five.index(number) : three_four_five.index(number) + 1] + ' '
        elif number in six_seven_eight:
            new_num += six_seven_eight[six_seven_eight.index(number) : six_seven_eight.index(number) + 1] + ' '
        elif number == nine:
            new_num += nine + ' '

    return new_num.strip()

