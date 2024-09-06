from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    words = numbers.split(" ")
    num_words = [number_to_word[num] for num in words]
    # Remove duplicates
    num_words = list(dict.fromkeys(num_words))
    num_words.sort()
    num_words = [word_to_number[num] for num in num_words]
    num_words = " ".join(num_words)
    return num_words


    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
