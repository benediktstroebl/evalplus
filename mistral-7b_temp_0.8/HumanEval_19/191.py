from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Write your code here.
    numbers_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    words = numbers.split(" ")
    new_words = []
    for i in range(len(words)):
        new_words.append(numbers_dict[words[i]])

    sorted_new_words = sorted(new_words)

    result = ""
    for i in range(len(sorted_new_words)):
        result += str(sorted_new_words[i]) + " "
    return result.strip()

