from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Traverse through the list
    for i in range(len(numbers)):
        # Get the rolling maximum
        rolling_max = numbers[i]
        # Get the maximum from the window
        for j in range(i):
            if j < len(numbers) - 1:
                if numbers[j] > numbers[j + 1]:
                    rolling_max = max(rolling_max, numbers[j])
        # Replace the current element with the rolling maximum
        numbers[i] = rolling_max
        # Remove the element from the window
        del numbers[i]
    return numbers

