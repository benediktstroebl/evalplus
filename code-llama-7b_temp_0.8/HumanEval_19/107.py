from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_list = [i.strip() for i in numbers.split()]
    string_list = []
    for number in number_list:
        if number == "zero":
            string_list.append(number)
        elif number == "one":
            string_list.append(number)
        elif number == "two":
            string_list.append(number)
        elif number == "three":
            string_list.append(number)
        elif number == "four":
            string_list.append(number)
        elif number == "five":
            string_list.append(number)
        elif number == "six":
            string_list.append(number)
        elif number == "seven":
            string_list.append(number)
        elif number == "eight":
            string_list.append(number)
        elif number == "nine":
            string_list.append(number)

    string_list.sort()
    return " ".join(string_list)

