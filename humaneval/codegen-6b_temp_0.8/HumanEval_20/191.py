from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest = min(numbers)
    largest = max(numbers)
    smallest_index = numbers.index(smallest)
    largest_index = numbers.index(largest)
    if smallest_index > largest_index:
        smallest_index, largest_index = largest_index, smallest_index
    numbers[smallest_index], numbers[largest_index] = numbers[largest_index], numbers[smallest_index]
    return numbers[smallest_index], numbers[largest_index]

