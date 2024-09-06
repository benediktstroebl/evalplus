from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far: Tuple[int, int] = (0, 0)
    max_so_far_pos = 0
    for pos, number in enumerate(numbers):
        max_so_far_pos += 1
        if max_so_far[0] < number:
            max_so_far = (number, max_so_far_pos)

    return [max_so_far[0] for _ in range(len(numbers))]

