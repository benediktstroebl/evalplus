from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    close = False
    for x in numbers:
        distance = math.sqrt(sum(x**2 for y in numbers if abs(x-y)<threshold))
        if distance < len(numbers)-1:
            close = close or True
    return close

