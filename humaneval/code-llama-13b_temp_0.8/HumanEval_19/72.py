from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    list_of_numbers = numbers.split()

    def get_index_of_number(number: str) -> int:
        if number == "zero":
            return 0
        elif number == "one":
            return 1
        elif number == "two":
            return 2
        elif number == "three":
            return 3
        elif number == "four":
            return 4
        elif number == "five":
            return 5
        elif number == "six":
            return 6
        elif number == "seven":
            return 7
        elif number == "eight":
            return 8
        elif number == "nine":
            return 9

    def get_index_of_number_in_list(number: str, numbers: List[str]) -> int:
        for i in range(0, len(numbers)):
            if numbers[i] == number:
                return i

    list_of_numbers.sort(key=lambda x: get_index_of_number(x))

    return " ".join(list_of_numbers)

