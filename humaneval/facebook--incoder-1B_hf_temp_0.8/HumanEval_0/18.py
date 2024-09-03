from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 3:
        return False

    length = len(numbers)
    diffs = []
    for i in range(length):
        prev = numbers[i - 1]
        next = numbers[i]
        if abs(prev - next) <= threshold:
            diffs.append(abs(prev - next))
        else:
            diffs.append(None)
    diffs.sort(reverse=True)
    return all(d == diffs[0] for d in diffs[1:])

