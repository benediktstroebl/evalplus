from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    maximum_value = numbers[0]
    max_sequence = [maximum_value]

    for number in numbers[1:]:
        if number > maximum_value:
            maximum_value = number

        max_sequence.append(maximum_value)

    return max_sequence

