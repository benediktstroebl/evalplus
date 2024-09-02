from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smaller, larger = float("inf"), float("-inf")
    for index, _ in enumerate(numbers):
        for index2, _ in enumerate(numbers):
            if numbers[index] != numbers[index2]:
                if abs(numbers[index] - numbers[index2]) < abs(smaller - larger):
                    smaller, larger = (
                        numbers[index],
                        numbers[index2],
                    ) if numbers[index] < numbers[index2] else (
                        numbers[index2], numbers[index])

    return smaller, larger

