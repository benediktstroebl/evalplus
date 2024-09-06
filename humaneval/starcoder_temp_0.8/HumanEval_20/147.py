from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2

    closest_difference = 1e100
    closest_elements = (numbers[0], numbers[1])

    for i, first_element in enumerate(numbers):
        for second_element in numbers[i+1:]:
            current_difference = abs(first_element - second_element)
            if current_difference < closest_difference:
                closest_difference = current_difference
                closest_elements = (first_element, second_element)

    return closest_elements

