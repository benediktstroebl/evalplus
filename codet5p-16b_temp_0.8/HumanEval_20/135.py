from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    number_of_elements = len(numbers)
    if number_of_elements < 2:
        raise ValueError("There must be at least two elements in the list.")

    first_closest_pair: List[float] = [None, None]
    second_closest_pair: List[float] = [None, None]

    for index in range(number_of_elements):
        if first_closest_pair[0] is None:
            first_closest_pair[0] = numbers[index]
            second_closest_pair[0] = numbers[index]
            continue

        if second_closest_pair[0] is None:
            second_closest_pair[0] = numbers[index]
            continue

        first_closest_pair[1] = numbers[index]
        second_closest_pair[1] = numbers[index]

        if abs(first_closest_pair[0] - first_closest_pair[1]) > abs(second_closest_pair[
