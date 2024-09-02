from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize running maximum
    max_running = numbers[-1]
    current_max = numbers[-1]
    previous_max = numbers[-1]

    # Keep track of current number
    current_number = numbers.pop(-1)

    # Update running maximum with current number
    max_running = max(max_running, current_number)

    # Add current number to the current max
    current_max.append(current_number)

    # Add the updated current max to the result
    result.append(current_max)

    # Add the last number to the current max
    current_max.append(numbers[-1])

    # Remove the last number from the sequence
    numbers.pop(-1)

    # Update the previous max with the last number
    previous_max = max(previous_max, numbers[-1])

    # Add the updated previous max to the result
    result.append(previous_max)

    return result

