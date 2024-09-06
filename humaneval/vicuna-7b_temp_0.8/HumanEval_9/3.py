from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_index = 0
    result = []
    for i in range(len(numbers) + 1):
        for j in range(i, len(numbers)):
            result.append(numbers[j])
        numbers = [x for x in numbers if x != result[-1]]
        result = [x for x in result if x != numbers[-1]]
        if len(result) == 0:
            max_index += 1
            result = [numbers[-1]]
    return result[:max_index]

