from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None

    for first_element_index, first_element in enumerate(numbers):
        for second_element_index, second_element in enumerate(numbers[first_element_index + 1 :]):
            difference = abs(first_element - second_element)
            if not closest_pair or difference < closest_pair[1]:
                closest_pair = (first_element, difference)

    return closest_pair

