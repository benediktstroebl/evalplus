from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the string into a list of numbers
    nums: List[str] = numbers.split(" ")

    # Convert the numbers to integers
    int_nums = [int(num) for num in nums]

    # Sort the numbers
    sorted_nums = sorted(int_nums)

    # Convert the numbers back to strings
    sorted_strs = [str(num) for num in sorted_nums]

    # Return the list of strings as a space-delimited string
    return " ".join(sorted_strs)

