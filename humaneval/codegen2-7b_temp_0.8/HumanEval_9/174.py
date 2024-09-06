from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return_numbers = []
    max_num = numbers[0]
    return_numbers.append(max_num)
    for number in numbers[1:]:
        if number > max_num:
            max_num = number
        return_numbers.append(max_num)
    return return_numbers
