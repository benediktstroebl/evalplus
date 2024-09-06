from typing import List
def sort_numbers(input_numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_numbers.split()
    sorted_numbers = 'zero' if numbers[0] != 'zero' else ''

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                if i == j:
                    sorted_numbers += numbers[i]
                else:
                    sorted_numbers += ' ' + numbers[i]

    return sorted_numbers