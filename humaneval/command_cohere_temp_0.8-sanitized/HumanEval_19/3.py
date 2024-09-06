from typing import List
def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = [int(char.lower()) for char in input_string.split()]
    sorted_numbers = [str(num) for num in numbers if num in range(0, 10)]
    return ' '.join(sorted_numbers)