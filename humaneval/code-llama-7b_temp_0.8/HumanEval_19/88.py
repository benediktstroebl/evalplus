from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert the string to a list of words
    words: List[str] = numbers.split()
    # Create a list of numbers
    numbers: List[int] = []
    for word in words:
        numbers.append(ord(word[0]) - 97)
    # Sort the numbers
    numbers.sort()
    # Create an output list
    output: List[str] = []
    for number in numbers:
        output.append(chr(number + 97))
    # Return the output list as a string
    return ' '.join(output)

