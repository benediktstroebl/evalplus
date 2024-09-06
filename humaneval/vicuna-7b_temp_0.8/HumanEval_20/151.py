from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    def _get_closest_numbers(numbers: List[float]) -> Tuple[float, float]:
        if not numbers:
            return numbers[0], numbers[0]

        min_dist = float("inf")
        closest_numbers = [numbers[0]]

        for num in numbers:
            dist = abs(num - numbers[0])
            if dist < min_dist:
                min_dist = dist
                closest_numbers = [num]

        return closest_numbers[0], closest_numbers[-1]

    return _get_closest_numbers(numbers)

