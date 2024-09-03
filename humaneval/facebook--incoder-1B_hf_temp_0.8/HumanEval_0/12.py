from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Filter out elements with zero length.
    numbers = [item for item in numbers if item!= 0]
    if not numbers:
        return False
    length = len(numbers)

    # Calculate distance between each two elements.
    dist = [abs(numbers[i] - numbers[j]) for j in range(length) if j!= i]

    # Check that all distances are below the threshold.
    return all(dist < threshold)

