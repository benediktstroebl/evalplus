from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_element, maximum = numbers[0], numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        else:
            if maximum < number:
                max_element, maximum = maximum, number

    return [max_element, maximum
