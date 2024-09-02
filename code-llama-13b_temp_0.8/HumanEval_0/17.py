from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Check if the first element is close to the second element
    if abs(numbers[0] - numbers[1]) <= threshold:
        return True

    # Check if the last element is close to the second last element
    if abs(numbers[len(numbers) - 1] - numbers[len(numbers) - 2]) <= threshold:
        return True

    # Check if any other element is close to its neighbor
    for i in range(1, len(numbers) - 1):
        if abs(numbers[i - 1] - numbers[i]) <= threshold or abs(numbers[i] - numbers[i + 1]) <= threshold:
            return True

    return False

