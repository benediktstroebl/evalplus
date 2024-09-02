from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # We use a list of tuples to store the rolling maximum found
    rolling_max_until_moment: List[Tuple[int, int]] = []

    # We get the length of the sequence
    n = len(numbers)

    # We iterate over the numbers
    for i in range(n):
        if i == 0:
            rolling_max_until_moment.append((numbers[i], i))
            continue

        current_number = numbers[i]
        max_number = max(current_number, rolling_max_until_moment[-1][0])
        position = rolling_max_until_moment[-1][1]
        rolling_max_until_moment.append((max_number, position))

    # We return the final list of rolling maximum elements found
    return [max_number for _, max_number in rolling_max_until_moment]

