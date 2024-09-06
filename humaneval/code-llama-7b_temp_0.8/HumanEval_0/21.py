from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Iterate over all numbers:
    for i in range(0, len(numbers) - 1):
        # Iterate over numbers after current number:
        for j in range(i + 1, len(numbers)):
            # Check if they are closer than threshold:
            if abs(numbers[i] - numbers[j]) < threshold:
                return True

    # No close pairs found:
    return False
