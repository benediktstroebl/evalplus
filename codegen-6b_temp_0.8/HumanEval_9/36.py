from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Default value for the result
    out = [None] * len(numbers)
    # Store all elements in the input array and their positions
    elements = {
        element: index
        for index, element in enumerate(numbers)
    }
    # Store last valid position
    last_valid_idx = 0
    # Loop over all elements
    for i, element in enumerate(numbers):
        # Try to find the next valid position
        next_valid_idx = last_valid_idx + 1
        while True:
            try:
                next_element = numbers[next_valid_idx]
                if next_element > element:
                    # Update position
                    last_valid_idx = next_valid_idx
                    next_valid_idx += 1
                else:
                    # Element does not have a valid position, keep searching
                    break
            except IndexError:
                # Reached the end of the array, skip this iteration
                break
        if last_valid_idx - i > 0:
            # Have at least one element in the sequence
            out[i] = numbers[last_valid_idx - i]
        else:
            # Element does not have a valid position, store the first element
            out[i] = element
    return out

