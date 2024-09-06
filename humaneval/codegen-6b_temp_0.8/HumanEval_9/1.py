from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # TODO: check if the given list is already max-sorted
    result = []
    if not numbers:
        return result
    max_number = max(numbers)
    result.append(max_number)
    if max_number == numbers[0]:
        return result
    number = numbers[0]
    for i in range(1, len(numbers)):
        if number < numbers[i]:
            result.append(number)
        else:
            number = numbers[i]
    return result

