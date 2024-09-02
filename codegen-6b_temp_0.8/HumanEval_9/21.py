from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    for index, num in enumerate(numbers):
        max_num = None
        for index_roll in range(index + 1, len(numbers) + 1):
            try:
                num_roll = numbers[index_roll - 1]
                if max_num is None or num_roll > max_num:
                    max_num = num_roll
            except IndexError:
                break
        result.append(max_num)
    return result

