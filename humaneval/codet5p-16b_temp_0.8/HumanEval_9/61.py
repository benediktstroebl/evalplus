from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_list: List[int] = []
    for index in range(len(numbers)):
        current_max = numbers[index]
        for number in numbers[index:]:
            if number > current_max:
                current_max = number
        max_list.append(current_max)
    return max_list

