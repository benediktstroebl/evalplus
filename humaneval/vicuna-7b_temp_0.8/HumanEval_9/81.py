from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = numbers[0]
    current_index = 0
    for number in numbers:
        if number > current_max:
            current_max = number
            current_index = 0
        if current_index < len(numbers) - 1:
            numbers[current_index] = current_max
            current_index += 1
    return numbers

