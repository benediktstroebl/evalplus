from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    nearest_neighbor_dist = 1
    is_close = False
    for num1, num2 in zip(numbers, numbers[1:]):
        distance = abs(num1 - num2)
        if distance < nearest_neighbor_dist:
            nearest_neighbor_dist = distance
            is_close = True
        else:
            nearest_neighbor_dist += 1
    return is_close

