from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # We will use a list to put the letters in that we input
    numbers_list = []

    for number in numbers:
        # We append the number to the numbers_list
        # We set the number to be the letter
        numbers_list.append(number)

    # We want to use the number list to sort
    # We want to sort from smallest to biggest
    # We will get the smallest number
    # We will set it to a
    smallest = min(numbers_list)

    # We will sort the numbers by using the minimum number

    for number in numbers_list:
        if number == smallest:
            numbers_list.remove(number)
            numbers_list.append(smallest)

    # We want to get the biggest number
    # We will set it to a
    biggest = max(numbers_list)

    # We want to sort the numbers by using the biggest number

    for number in numbers_list:
        if number == biggest:
            numbers_list.remove(number)
            numbers_list.append(biggest)

    # We want to get the numbers that are left

    numbers_list.sort()

    # We want to send the number to a string
    new_number = ""

    # We will use a while loop to get the numbers
    # We want to start at the first number

    while numbers_list:
        # We get the first number
        this_number = numbers_list.pop(0)

        # We want to add the number to the string
        new_number += this_number

    return new_number

