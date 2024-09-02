from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    result = []
    number_list = numbers.split()
    for num in number_list:
        if num == "zero":
            result.append(0)
        elif num == "one":
            result.append(1)
        elif num == "two":
            result.append(2)
        elif num == "three":
            result.append(3)
        elif num == "four":
            result.append(4)
        elif num == "five":
            result.append(5)
        elif num == "six":
            result.append(6)
        elif num == "seven":
            result.append(7)
        elif num == "eight":
            result.append(8)
        elif num == "nine":
            result.append(9)
        else:
            print("Invalid input!")
            return None
    result = sorted(result)
    result = " ".join(str(x) for x in result)
    return result

