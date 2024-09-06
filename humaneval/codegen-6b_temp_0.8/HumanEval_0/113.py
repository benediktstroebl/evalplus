from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    from collections import defaultdict

    threshold_squared = threshold ** 2
    counts = defaultdict(int)
    for n in numbers:
        counts[n] += 1
    for n in numbers:
        for i, m in enumerate(numbers):
            if i == n:
                continue
            if m > n:
                y = m - n
            else:
                y = m + n
            if y ** 2 < threshold_squared:
                if counts[i] == 1:
                    counts[i] = 2
                else:
                    counts[i] -= 1
    return any(count == 1 for count in counts.values())

