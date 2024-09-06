from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_list = numbers.split()
    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if number_list[j] == "zero":
                continue
            if number_list[i] == "zero":
                continue
            elif number_list[i] == "one" and number_list[j] == "two":
                continue
            elif number_list[i] == "one" and number_list[j] == "three":
                continue
            elif number_list[i] == "one" and number_list[j] == "four":
                continue
            elif number_list[i] == "one" and number_list[j] == "five":
                continue
            elif number_list[i] == "one" and number_list[j] == "six":
                continue
            elif number_list[i] == "one" and number_list[j] == "seven":
                continue
            elif number_list[i] == "one" and number_list[j] == "eight":
                continue
            elif number_list[i] == "one" and number_list[j] == "nine":
                continue
            elif number_list[i] == "two" and number_list[j] == "three":
                continue
            elif number_list[i] == "two" and number_list[j] == "four":
                continue
            elif number_list[i] == "two" and number_list[j] == "five":
                continue
            elif number_list[i] == "two" and number_list[j] == "six":
                continue
            elif number_list[i] == "two" and number_list[j] == "seven":
                continue
            elif number_list[i] == "two" and number_list[j] == "eight":
                continue
            elif number_list[i] == "two" and number_list[j] == "nine":
                continue
            elif number_list[i] == "three" and number_list[j] == "four":
                continue
            elif number_list[
