from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input
    numbers = numbers.split(' ')
    # Create a dictionary with the numbers as the keys
    number_dict = {}
    for i in range(10):
        number_dict[str(i)] = i
    # Iterate through the numbers
    for number in numbers:
        # Remove anything that is not a number
        number = ''.join([char for char in number if char.isdigit()])
        number_dict[number] = int(number)
    # This creates a list of the keys
    dict_keys = list(number_dict.keys())
    # Sort the list from smallest to largest
    dict_keys.sort()
    # Recreate the dictionary with sorted keys
    new_dict = {}
    for key in dict_keys:
        new_dict[key] = number_dict[key]
    # Get the sorted list
    sorted_numbers = []
    for key in dict_keys:
        sorted_numbers.append(key)
    sorted_numbers = ' '.join(sorted_numbers)
    return sorted_numbers

