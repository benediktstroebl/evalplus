from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_of_previous_numbers = numbers[0]
    max_of_this_number = numbers[0]
    output = [max_of_this_number]
    for number in numbers[1:]:
        if number > max_of_previous_numbers:
            max_of_previous_numbers = number
        max_of_this_number = max(max_of_this_number, number)
        output.append(max_of_this_number)
    return output

