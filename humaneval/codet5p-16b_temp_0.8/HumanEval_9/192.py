from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Create an empty list to store the rolling maximum until given moment
    rolling_max: List[int] = []
    # Create an auxiliary variable to store the maximum number from the beginning of the sequence
    max_number: int = numbers[0]
    # Iterate through the given list
    for current_number in numbers:
        # Generate the rolling maximum until given moment
        rolling_max.append(max_number)
        # Save the current number as the maximum
        max_number = max(max_number, current_number)
    return rolling_max

