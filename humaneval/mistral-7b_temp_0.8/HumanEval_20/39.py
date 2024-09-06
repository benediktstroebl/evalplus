from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Numbers list is too short")

    def diff_to_closest(x: float):
        diff_to_closest = None
        for y in numbers:
            if diff_to_closest is None:
                diff_to_closest = abs(x - y)
            elif abs(x - y) < diff_to_closest:
                diff_to_closest = abs(x - y)

        return diff_to_closest

    closest_1 = min(numbers, key=diff_to_closest)
    closest_2 = min(numbers, key=lambda x: abs(x - closest_1))

    return closest_1, closest_2
