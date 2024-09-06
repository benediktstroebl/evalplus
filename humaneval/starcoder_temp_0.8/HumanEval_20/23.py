from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest = numbers[0]
    smallest_difference = numbers[1] - numbers[0]
    for number in numbers:
        if number!= smallest:
            current_difference = number - smallest
            if current_difference < smallest_difference:
                smallest_difference = current_difference
                smallest = number
    return smallest, smallest + smallest_difference

