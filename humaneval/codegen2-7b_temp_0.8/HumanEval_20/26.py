from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) > 1
    smallest = numbers[0]
    smallest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest_index = i
            smallest = numbers[i]
    second_smallest = smallest
    second_smallest_index = smallest_index
    for i in range(0, smallest_index):
        if numbers[i] > second_smallest:
            second_smallest = numbers[i]
            second_smallest_index = i
    return smallest_index, second_smallest_
