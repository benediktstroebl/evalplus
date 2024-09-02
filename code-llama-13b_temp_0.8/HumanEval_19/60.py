from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split the numbers on spaces into a list
    # you can also use the built-in split method:
    # numbers = numbers.split(' ')
    numbers_list = [n for n in numbers.split()]

    # create a list of 0-9 in order
    numbers_order = [str(i) for i in range(10)]

    # create an empty list for sorting
    sorted_numbers = []

    # create a list for unsorted numbers
    unsorted_numbers = []

    # create a list for any numbers that are not 0-9
    invalid_numbers = []

    # loop over the list of numbers
    # if the number is in the correct order, add it to sorted_numbers
    # otherwise, add it to unsorted_numbers
    for number in numbers_list:
        if number in numbers_order:
            sorted_numbers.append(number)
        else:
            unsorted_numbers.append(number)

    # sort unsorted_numbers
    sorted_unsorted_numbers = sorted(unsorted_numbers)

    # add sorted_unsorted_numbers to sorted_numbers
    sorted_numbers.extend(sorted_unsorted_numbers)

    # return the sorted_numbers in order, space-delimited
    return ' '.join(sorted_numbers)

