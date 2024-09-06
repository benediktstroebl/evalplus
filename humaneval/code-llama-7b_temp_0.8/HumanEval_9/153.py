from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_numbers: List[int] = []
    current_max_number: int = numbers[0]
    for number in numbers:
        if number > current_max_number:
            current_max_number = number
        rolling_max_numbers.append(current_max_number)
    return rolling_max_numbers

