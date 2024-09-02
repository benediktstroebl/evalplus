from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    sorted_numbers = sorted(numbers)
    for index, current_number in enumerate(sorted_numbers):
        next_index = index + 1
        while next_index < len(sorted_numbers):
            next_number = sorted_numbers[next_index]
            if abs(current_number - next_number) < threshold:
                return True
            next_index += 1
    return False

