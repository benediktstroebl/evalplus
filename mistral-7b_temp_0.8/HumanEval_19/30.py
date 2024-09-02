from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Step 1: create an empty list
    number_list = []
    # Step 2: split the string into a list of words
    words = numbers.split()
    # Step 3: convert each word to a number
    for word in words:
        number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[word]
        number_list.append(number)
    # Step 4: sort the list
    sorted_number_list = sorted(number_list)
    # Step 5: convert the sorted list back to a string
    sorted_string = ""
    for num in sorted_number_list:
        sorted_string += {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9
