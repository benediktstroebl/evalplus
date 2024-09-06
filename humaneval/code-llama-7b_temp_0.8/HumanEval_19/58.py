from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # 1) Convert string to list of numberals
    numberals = numbers.split()

    # 2) create an empty list to store sorted numberals
    sorted_numberals = []

    # 3) Iterate over the list of numberals
    for _ in numberals:
        for number in numberals:
            # 4) convert numberals to integer
            if number == 'zero':
                number_integer = 0
            if number == 'one':
                number_integer = 1
            if number == 'two':
                number_integer = 2
            if number == 'three':
                number_integer = 3
            if number == 'four':
                number_integer = 4
            if number == 'five':
                number_integer = 5
            if number == 'six':
                number_integer = 6
            if number == 'seven':
                number_integer = 7
            if number == 'eight':
                number_integer = 8
            if number == 'nine':
                number_integer = 9
            # 5) append to the sorted list
            if number_integer not in sorted_numberals:
                sorted_numberals.append(number_integer)
            else:
                pass

    # 6) convert the sorted list to string
    sorted_string = " ".join(str(e) for e in sorted_numberals)

    return sorted_string

