from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    dict = {"one": "one", "two": "two", "three": "three",
            "four": "four", "five": "five", "six": "six", "seven": "seven", "eight": "eight", "nine": "nine"}
    for key in dict:
        numbers = numbers.replace(key, dict[key])

    # Split string
    split_numbers = numbers.split()

    # Replace ints with strings
    for index, item in enumerate(split_numbers):
        split_numbers[index] = int(item)

    # Sort numbers
    split_numbers.sort()

    # Rejoin to string
    numbers = ""
    for item in split_numbers:
        numbers += str(item)

    return numbers

