from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 1:
        return numbers

    rolling_max_numbers = []
    previous_max_num = numbers[0]

    for n in numbers:
        if n > previous_max_num:
            rolling_max_numbers.append(n)
        else:
            rolling_max_numbers.append(previous_max_num)

        previous_max_num = n

    return rolling_max_numbers

