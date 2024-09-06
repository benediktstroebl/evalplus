from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the input string into a list of words
    words = numbers.split()
    
    # convert the words to lowercase
    words = [word.lower() for word in words]
    
    # convert the words to numbers
    numbers = [int(word) for word in words]
    
    # sort the numbers in ascending order
    numbers.sort()
    
    # convert the numbers back to words
    words = [word for word in numbers]
    
    # join the words back into a string
    return ' '.join(words)
