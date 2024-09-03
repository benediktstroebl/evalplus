from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) == 0:
        return False

    closed = []
    current = 0
    while current < len(numbers):
        current = current + 1
        if current == len(numbers):
            break

        last = numbers[current-1]
        next_two = numbers[current+1]

        if abs(current - current-2) <= threshold:
            if last < next_two:
                closed.append(True)
            else:
                closed.append(False)
        else:
            if last > next_two:
                closed.append(True)
            else:
                closed.append(False)

    return any(closed)

