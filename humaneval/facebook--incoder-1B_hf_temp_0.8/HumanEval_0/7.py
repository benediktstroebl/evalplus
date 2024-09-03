from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    close_pairs = []
    for number, index in zip(numbers, range(len(numbers))):
        if abs(number - numbers[index + 1]) < threshold:
            close_pairs.append((number, index + 1, numbers[index]))
    return any(p[0] == p[1] and p[2] > p[1] for p in close_pairs)

