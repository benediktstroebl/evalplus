from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) <= 1:
        return numbers

    else:
        # Get the rolling maximum element found in the previous step
        current_max = numbers[-1]
        numbers.pop()
        # Calculate the rolling maximum element until the previous step
        previous_numbers = [current_max]
        previous_max = current_max

        for i in range(1, len(numbers)):
            number = numbers[i]
            previous_numbers.append(previous_max)
            if number > previous_max:
                previous_max = number
        return previous_numbers