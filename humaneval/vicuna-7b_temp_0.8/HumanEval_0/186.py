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

    closest_diff = max(
        abs(numbers[0] - numbers[1]),
        abs(numbers[0] - numbers[2]),
        abs(numbers[1] - numbers[2]),
    )

    if closest_diff < threshold * 0.5:
        return False

    closer_pairs = []
    for i in range(3, len(numbers)):
        for j in range(i + 1, len(numbers)):
            closer_diff = abs(numbers[i] - numbers[j])
            if closer_diff < threshold and closer_diff < closest_diff:
                closer_pairs.append((numbers[i], numbers[j]))
            else:
                break

    if len(closer_pairs) >= 2:
        return True
    return False

