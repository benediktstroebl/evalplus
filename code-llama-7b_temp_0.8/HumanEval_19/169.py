from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if numbers == "":
        return numbers
    number_array = []
    for number in numbers.split():
        if number == "zero" or number == "zero ":
            number_array.append(0)
        elif number == "one" or number == "one ":
            number_array.append(1)
        elif number == "two" or number == "two ":
            number_array.append(2)
        elif number == "three" or number == "three ":
            number_array.append(3)
        elif number == "four" or number == "four ":
            number_array.append(4)
        elif number == "five" or number == "five ":
            number_array.append(5)
        elif number == "six" or number == "six ":
            number_array.append(6)
        elif number == "seven" or number == "seven ":
            number_array.append(7)
        elif number == "eight" or number == "eight ":
            number_array.append(8)
        elif number == "nine" or number == "nine ":
            number_array.append(9)
    number_array.sort()
    for number in number_array:
        if number == 0:
            number = "zero"
        elif number == 1:
            number = "one"
        elif number == 2:
            number = "two"
        elif number == 3:
            number = "three"
        elif number == 4:
            number = "four"
        elif number == 5:
            number = "five"
        elif number == 6:
            number = "six"
        elif number == 7:
            number = "seven"
        elif number == 8:
            number = "eight"
        elif number == 9:
            number = "nine"
        numbers = numbers.replace(number, "", 1)
        numbers = numbers + number + " "
    return numbers

