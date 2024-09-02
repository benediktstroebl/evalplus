from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # List of rolling maximum integers
    result = []

    # If the list is empty, return an empty list
    if len(numbers) == 0:
        return result

    # Maximum integer
    maximum = numbers[0]
    # Iterate over the numbers
    for number in numbers:
        # If current number is greater than current maximum
        if number > maximum:
            # Set current number as the maximum
            maximum = number
        # Append maximum to the result
        result.append(maximum)

    return result

