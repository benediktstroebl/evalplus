from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_num = numbers[0]
    results: List[int] = [max_num]
    for num in numbers:
        max_num = max(num, max_num)
        results.append(max_num)
    return results

