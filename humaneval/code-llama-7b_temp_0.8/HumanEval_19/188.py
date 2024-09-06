from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    def split(text: str) -> List[str]:
        return text.split()

    def sort_words(words: List[str]) -> List[str]:
        return sorted(words)

    def join(words: List[str]) -> str:
        return " ".join(words)

    return join(sort_words(split(numbers)))

