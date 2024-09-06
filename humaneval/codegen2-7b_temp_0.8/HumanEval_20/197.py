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
        raise ValueError(f"length of numbers must be at least 2 but was {len(numbers)}")
    smallest = min(numbers)
    largest = max(numbers)
    if smallest == largest:
        return smallest, smallest
    closest_index = (numbers.index(smallest), numbers.index(largest))
    smallest_index = closest_index[0]
    largest_index = closest_index[1]
    return numbers[smallest_index], numbers[largest_index
