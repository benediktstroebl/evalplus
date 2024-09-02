from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Create empty list to store the rolling maximum values
    rolling_max_values = []

    # Keep track of the last maximum element found
    last_max = numbers[0]

    # Initialize a variable to keep track of the current index
    current_index = 0

    # Iterate through the list of numbers
    for number in numbers:
        # Update the last maximum element if the current element is greater than the previous maximum element
        if number > last_max:
            last_max = number
            rolling_max_values.append(last_max)
            current_index += 1

        # Add the current element to the list of numbers
        numbers.insert(current_index, number)

        # Update the current index
        current_index += 1

    # Return the list of rolling maximum values
    return rolling_max_values

