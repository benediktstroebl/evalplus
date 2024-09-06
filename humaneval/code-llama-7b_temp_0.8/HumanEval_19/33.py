from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # print(numbers)
    my_numbers = numbers.split()
    for _ in range(len(my_numbers) - 1):
        for i in range(len(my_numbers) - 1):
            if (
                my_numbers[i] == "zero"
                and my_numbers[i + 1] == "one"
                or my_numbers[i] == "one"
                and my_numbers[i + 1] == "two"
                or my_numbers[i] == "two"
                and my_numbers[i + 1] == "three"
                or my_numbers[i] == "three"
                and my_numbers[i + 1] == "four"
                or my_numbers[i] == "four"
                and my_numbers[i + 1] == "five"
                or my_numbers[i] == "five"
                and my_numbers[i + 1] == "six"
                or my_numbers[i] == "six"
                and my_numbers[i + 1] == "seven"
                or my_numbers[i] == "seven"
                and my_numbers[i + 1] == "eight"
                or my_numbers[i] == "eight"
                and my_numbers[i + 1] == "nine"
            ):
                my_numbers[i], my_numbers[i + 1] = my_numbers[i + 1], my_numbers[i]
    return " ".join(my_numbers)

