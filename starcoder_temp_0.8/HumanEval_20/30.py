from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2, "List must be of length 2 or more"
    min_delta = float("inf")
    for index, n in enumerate(numbers):
        for m in numbers[index + 1 :]:
            delta = abs(n - m)
            if delta < min_delta:
                min_delta = delta
                min_index = index
                max_index = index + 1 + numbers[index + 1 :].index(m)

    return numbers[min_index], numbers[max_index]

