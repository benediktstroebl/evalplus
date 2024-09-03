from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False
    length = len(numbers)
    two_numbers = []
    for i in range(1, length):
        num = numbers[i - 1]
        two_num = numbers[i - 1] * 2
        if abs(num - two_num) < threshold:
            two_numbers.append(two_num)
    if two_numbers:
        return True
    else:
        return False

