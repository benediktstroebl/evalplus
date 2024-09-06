from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # TODO: Implement the function using a list to store the input numbers and then returning the sorted list.
    # Input: 'three one five'
    # Output: 'one three five'
    # The output is obtained by sorting the input string in place
    # Using a list to store the input numbers
    input_numbers = [int(x) for x in numbers.split()]
    # Sorting the input numbers from smallest to largest
    input_numbers.sort()
    # Reversing the sorted list
    input_numbers.reverse()
    # Joining the sorted input numbers back to the original string
    return ' '.join(map(str, input_numbers))

