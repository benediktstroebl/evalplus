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
    close_set = set()
    for number in numbers:
        dist = abs(number - number)
        close_set.add((number, dist))
    close_list = [(number, dist) for number, dist in close_set if dist <= threshold]
    return len(close_list) == 1

