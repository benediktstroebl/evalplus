from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # get all the number strings in a list
    number_list = numbers.split()
    # get a list of all the numbers from zero to nine
    number_choices = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    # define a function that will check if the current number is in the list of number choices
    def check_if_in_list(number, number_list):
        if number in number_list:
            return True
        else:
            return False

    # define a function that will sort the number_list in place
    def sort_list_in_place(number_list):
        for i in range(len(number_list) - 1):
            for j in range(len(number_list) - 1 - i):
                if number_choices.index(number_list[j]) > number_choices.index(
                    number_list[j + 1]
                ):
                    # swap the numbers around
                    number_list[j], number_list[j + 1] = (
                        number_list[j + 1],
                        number_list[j],
                    )

    # loop through the list of numbers and remove any numbers that are not in the number_choices list
    for number in number_list:
        # if the number is not in the list of number choices, remove it
        if check_if_in_list(number, number_choices) == False:
            number_list.remove(number)

    # sort the number list in place
    sort_list_in_place(number_list)

    # return the sorted list as a string
    return " ".join(number_list)

