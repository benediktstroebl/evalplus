from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Find the minimum and maximum
    max_diff = float('-inf')
    min_diff = float('inf')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = numbers[j] - numbers[i]
            if diff < min_diff:
                min_diff = diff
            if diff > max_diff:
                max_diff = diff
    if min_diff <= threshold < max_diff:
        return True
    else:
        return False

