from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # if list is empty
    if not numbers:
        return numbers
    # initializing first element of rolling maximum list with first element of sequence
    rolling_max_numbers = [numbers[0]]
    # iterating from second element of sequence
    for index in range(1, len(numbers)):
        # if current element is less than previous element (rolling maximum), add previous element to list,
        # else add current element to list
        rolling_max_numbers.append(max(rolling_max_numbers[index - 1], numbers[index]))
    return rolling_max_numbers

