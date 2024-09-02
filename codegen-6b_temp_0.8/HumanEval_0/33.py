from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) <= 1:
        return False

    # Find subarray of two consecutive items
    def find_subarray(array: List[float], threshold: float) -> int:
        for i in range(1, len(array)):
            if abs(array[i - 1] - array[i]) <= threshold:
                return i

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if find_subarray(numbers[i:i + j], threshold) is not None:
                return True

    return False

