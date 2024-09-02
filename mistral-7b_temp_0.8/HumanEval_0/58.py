from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Check if there are at least two numbers in given list
    if len(numbers) < 2:
        return False
    # Create a list of differences between all pairs of numbers in given list
    differences = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            differences.append(difference)
    # Find minimum and maximum values in difference list
    minimum = min(differences)
    maximum = max(differences)
    # Return true if given list has any two numbers closer to each other than threshold
    return minimum < threshold
