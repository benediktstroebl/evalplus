from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if not numbers or len(numbers) < 2:
        return None, None
    else:
        smallest_distance = min(numbers)
        smallest_index = numbers.index(smallest_distance)

        second_smallest_distance = min(numbers[smallest_index:])
        second_smallest_index = smallest_index + numbers[smallest_index:].index(
            second_smallest_distance
        )
        return numbers[smallest_index], numbers[second_smallest_index
