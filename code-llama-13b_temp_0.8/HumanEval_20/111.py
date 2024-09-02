from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Solution below is based on the knowledge of the fact that list is mutable and we can sort it in place
    # using `sort` method.
    numbers.sort()
    min_distance: float = float('inf')
    closest_elements: Tuple[float, float] = (0.0, 0.0)
    for index in range(1, len(numbers)):
        current_distance = numbers[index] - numbers[index - 1]
        if current_distance < min_distance:
            min_distance = current_distance
            closest_elements = (numbers[index - 1], numbers[index])
    return closest_elements

