from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize the return list with empty values
    result = [0] * len(numbers)

    # Initialize the index to start with
    index = 0

    # While the value at the current index is not less than the maximum value so far
    while numbers[index] <= max(result):
        # Append the value at the current index to the result list
        result[index] = numbers[index]

        # Update the index to the next value
        index += 1

    # Return the result list
    return result

