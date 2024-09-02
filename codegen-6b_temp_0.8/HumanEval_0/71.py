from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # TODO: this seems to be lower and more efficient.
    # loop through array, if previous element is not equal to current element,
    # increment previous index and previous element, and decrement current index and current element
    # if that's the case, we have found a pair within threshold of each other.

    for idx in range(len(numbers) - 1):
        if numbers[idx] != numbers[idx + 1]:
            idx_1, idx_2 = idx, idx + 1
            close_to_1 = abs(numbers[idx_2] - numbers[idx_1]) <= threshold
            close_to_2 = abs(numbers[idx_1] - numbers[idx_2]) <= threshold

            if close_to_1 and close_to_2:
                return True

    return False

