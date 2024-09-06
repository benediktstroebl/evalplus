from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # valid_choices = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    #
    # num_list = [valid_choices.index(x) for x in numbers.split()]
    #
    # return " ".join(list(map(lambda x: valid_choices[x], sorted(num_list))))

    return " ".join(sorted(numbers.split(), key=lambda x: numbers.split().index(x)))

