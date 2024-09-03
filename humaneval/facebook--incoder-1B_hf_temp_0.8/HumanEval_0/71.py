from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers_len = len(numbers)
    assert numbers_len > 0
    assert len(numbers) == numbers_len
    assert all(number >= threshold for number in numbers)

    prev_distance = numbers[0]
    for number in numbers[1:]:
        curr_distance = number - prev_distance
        if abs(curr_distance) <= threshold:
            return True
        prev_distance = curr_distance
    return False

