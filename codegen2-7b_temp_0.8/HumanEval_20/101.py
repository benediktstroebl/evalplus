from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    def find_closest(number: float) -> Tuple[float, float]:
        def distance_to_closest(number: float) -> float:
            if number == closest:
                return 0.0
            return (number - closest) ** 2

        closest = min(numbers, key=distance_to_closest)
        return closest, numbers.count(closest)

    if len(numbers) < 2:
        raise ValueError("numbers must be of length at least two")

    return find_closest(min(numbers))

