from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # TODO: Replace the pass statement with your code.
    # Note: You may need to use a for loop, a while loop, a conditional statement,
    # list slicing, and string concatenation.
    # Passed in a string of numbers
    numbers_list = numbers.split(" ")

    for index in range(len(numbers_list)):
        smallest = numbers_list[index]
        small_index = index
        for i in range(index, len(numbers_list)):
            if numbers_list[i] < smallest:
                smallest = numbers_list[i]
                small_index = i
        # Swap the smallest element to the index
        numbers_list[small_index], numbers_list[index] = numbers_list[index], numbers_list[small_index]
    # Concatenate the numbers
    new_string = ""
    for number in numbers_list:
        new_string += number
    return new_string

