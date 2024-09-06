from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Create empty list to store rolling maximum
    rolling_max_list = []
    # Get the length of the input list
    n = len(numbers)
    # Iterate through each number in the list
    for i in range(n):
        # Store the maximum element found so far
        current_max = numbers[i]
        # Find the maximum element starting from the next element in the list
        for j in range(i + 1, n):
            if numbers[j] > current_max:
                current_max = numbers[j]
        # Add the current maximum element to the rolling_max list
        rolling_max_list.append(current_max)
    return rolling_max_list

