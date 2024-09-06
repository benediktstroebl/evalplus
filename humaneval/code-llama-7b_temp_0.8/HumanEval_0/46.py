from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if threshold > 1:
        raise ValueError(
            f"The threshold must be between 0 and 1, got {threshold}"
        )

    # Set to True when we find two numbers that are less or equal to the threshold
    close_numbers = False

    # Compare each number with every number after it
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance <= threshold:
                close_numbers = True

    return close_numbers
