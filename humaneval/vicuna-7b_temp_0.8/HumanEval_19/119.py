from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the string into a list of words
    words = numbers.split()

    # convert the words to lowercase
    words = [word.lower() for word in words]

    # sort the words by converting them to integers and comparing them
    words = sorted(list(map(int, words)))

    # convert the sorted words back to strings
    words = [str(word) for word in words]

    # join the words back into a single string
    return " ".join(words)
