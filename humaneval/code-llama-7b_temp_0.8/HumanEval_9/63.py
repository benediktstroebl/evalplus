from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    answer = []
    max_so_far = None
    for i, n in enumerate(numbers):
        if max_so_far is None or n >= max_so_far:
            max_so_far = n
        answer.append(max_so_far)
    return answer

