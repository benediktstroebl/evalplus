from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()
    for curr_i, curr_num in enumerate(numbers):
        smallest = numbers[curr_i]
        for other_i in range(curr_i, len(numbers)):
            other_num = numbers[other_i]
            if abs(curr_num - other_num) < threshold:
                return True
            elif abs(curr_num - other_num) < smallest * 1.05:
                smallest = other_num
    return False

