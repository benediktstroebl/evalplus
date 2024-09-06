from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    if len(numbers) == 1:
        return numbers

    max_so_far = numbers[0]
    max_so_far_list = [numbers[0]]

    for number in numbers[1:]:
        max_so_far = max(max_so_far, number)
        max_so_far_list.append(max_so_far)

    return max_so_far_list

