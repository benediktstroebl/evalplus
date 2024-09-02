from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # finding the smallest number
    smallest_number = min(numbers)
    # finding the largest number
    largest_number = max(numbers)

    if abs(smallest_number - largest_number) == 0:
        return smallest_number, largest_number

    number_set = {
        (abs(smallest_number - largest_number), smallest_number, largest_number)
    }

    for number in numbers:
        if number != smallest_number and number != largest_number:
            number_set.add((abs(number - smallest_number), number, smallest_number))
            number_set.add((abs(number - largest_number), number, largest_number))

    sorted_set = sorted(number_set)

    return sorted_set[0][1], sorted_set[0][2]

