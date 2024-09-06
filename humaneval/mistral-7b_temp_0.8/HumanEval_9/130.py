from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return list(
        map(
            lambda prev_max, cur: cur if prev_max <= cur else prev_max,
            zip([0], numbers[:1]),
            numbers[1:]
        )
    )

