from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if not numbers:
        return False

    numbers.sort()

    for i in range(len(numbers)):
        left = i + 1

        while left < len(numbers) and numbers[left] - threshold <= numbers[i]:
            left += 1

        if left == len(numbers):
            return False

        right = left - 1

        while right > 0 and numbers[right] - threshold <= numbers[left]:
            right -= 1

        return right != left

