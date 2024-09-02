from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Trivial case
    if not numbers:
        return []

    # If list is empty, return
    if len(numbers) == 0:
        return numbers

    # Set rolling max = first element
    rolling_max = numbers[0]
    result = [rolling_max]

    for i in range(1, len(numbers)):
        if numbers[i] > rolling_max:
            rolling_max = numbers[i]
        result.append(rolling_max)

    return result

