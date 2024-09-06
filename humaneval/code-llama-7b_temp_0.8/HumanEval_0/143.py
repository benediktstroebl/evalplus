from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Iterate through the list, and compare each element with its previous element.
    # If the difference is smaller than the threshold, return True.
    # If we reach the end of the list, return False.
    for i, elem in enumerate(numbers):
        if i == 0:
            continue
        previous = numbers[i - 1]
        diff = abs(previous - elem)
        if diff < threshold:
            return True
    return False

