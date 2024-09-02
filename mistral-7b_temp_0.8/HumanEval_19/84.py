from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # The elements of numbers are: 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    # Create a list of those elements.
    list_of_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # Create an empty list called ordered_numbers.
    ordered_numbers = []
    # Create a variable called count that stores the index of the next element to be extracted from the string numbers.
    count = 0
    # While count is less than the length of numbers:
    while count < len(numbers):
        # Add the element at the index of numbers that is count to the ordered_numbers list.
        ordered_numbers.append(numbers[count])
        # Increment count by one.
        count += 1
    # Create a variable called sorted_numbers that stores the result of calling sorted on the list ordered_numbers.
    sorted_numbers = sorted(ordered_numbers)
