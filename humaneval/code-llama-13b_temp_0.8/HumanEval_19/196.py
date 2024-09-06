from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if len(numbers) == 0:
        return 'zero'
    # first we split the string
    numbers = numbers.split()
    # we create a list of dictionaries from the original list of numberals
    numbers_dict = []
    for number in numbers:
        numbers_dict.append({number: 0})
    # we create a list of integers from the original list of numberals
    numbers_int = []
    for number in numbers:
        numbers_int.append(eval(number))
    # we sort the list of integers
    numbers_int.sort()
    # we create a new list of numberals
    numbers_sorted = []
    # we use the sorted list of integers and the original dictionary list
    # to create a new list of numberals
    for number in numbers_int:
        for dict_number in numbers_dict:
            for k, v in dict_number.items():
                if number == v:
                    numbers_sorted.append(k)
    return ' '.join(numbers_sorted)

