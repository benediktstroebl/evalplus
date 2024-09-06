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
        return (-1, -1)
    else:
        smallest = float('inf')
        second_smallest = float('inf')
        for i in range(len(numbers)):
            if abs(numbers[i]) < smallest:
                second_smallest = smallest
                smallest = abs(numbers[i])
            elif abs(numbers[i]) < second_smallest:
                second_smallest = abs(numbers[i])
        return (smallest, second_small
