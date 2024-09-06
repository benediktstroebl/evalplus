from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # If the list is empty or one element, return the element
    if len(numbers) <= 1:
        return numbers

    # Initialize the rolling maximum element and the start index
    max_value = numbers[0]
    start_index = 0

    # Iterate over the list and update the rolling maximum element and the start index
    for index in range(1, len(numbers)):
        # If the current element is greater than the rolling maximum element, update the rolling maximum element and the start index
        if numbers[index] > max_value:
            max_value = numbers[index]
            start_index = index

    # Return the rolling maximum element and the start index
    return [max_value, start_index]

