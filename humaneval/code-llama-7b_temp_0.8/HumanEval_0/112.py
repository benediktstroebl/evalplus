from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Traverse through the list and check if the number and its next number are less than the threshold
    # away from each other
    for index, number in enumerate(numbers):
        # The last number can't be compared with the next number so skip it
        if index == len(numbers) - 1:
            break
        if abs(numbers[index] - numbers[index + 1]) < threshold:
            return True

    return False

