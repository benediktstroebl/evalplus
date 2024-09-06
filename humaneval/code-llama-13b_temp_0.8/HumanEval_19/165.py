from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # end_of_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # return " ".join(sorted(numbers.split(), key=end_of_num.index))
    # Other solutions that are not using predefined functions and lists
    return " ".join(sorted(words.strip() for words in numbers.split()))

