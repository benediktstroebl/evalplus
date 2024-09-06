from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    number_to_index = {}
    for i, num in enumerate(numbers):
        number_to_index[num] = i

    for i, num_1 in enumerate(numbers):
        for num_2 in numbers[i + 1 :]:
            if abs(num_2 - num_1) < threshold:
                return True

    return False
