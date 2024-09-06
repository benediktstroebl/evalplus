from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_dict = {
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
    words = numbers.split()
    words_as_ints = []
    for word in words:
        words_as_ints.append(number_dict[word])
    sorted_ints = sorted(words_as_ints)
    sorted_words = []
    for number in sorted_ints:
        sorted_words.append(str(number))
    return ' '.join(sorted_words)

