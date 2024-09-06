from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_list: List[int] = []
    index: int = 0
    while index < len(numbers) - 1:
        new_max: int = numbers[index]
        for number in numbers[index + 1:]:
            if new_max < number:
                new_max = number
        max_list.append(new_max)
        index += 1

    max_list.append(numbers[-1])
    return max_list

