from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_sorted = sorted(numbers)
    closest_numbers = [numbers_sorted[0], numbers_sorted[1]]

    for i in numbers_sorted:
        for j in numbers_sorted:
            if i == j:
                pass
            else:
                closest_distance = abs(j - i)
                closest_numbers_distance = abs(closest_numbers[1] - closest_numbers[0])
                if closest_distance < closest_numbers_distance:
                    closest_numbers = [j, i]
    return closest_numbers[0], closest_numbers[1]

