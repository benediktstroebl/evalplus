from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_counter = Counter()
    max_numbers = []
    for number in numbers:
        max_counter[number] = max(max_counter.get(number, 0), number)
        max_numbers.append(number)

    while max_counter:
        return max_numbers[-1]

    return 0

