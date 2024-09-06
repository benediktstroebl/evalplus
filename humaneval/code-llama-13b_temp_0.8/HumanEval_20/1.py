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
    number_a = numbers[0]
    number_b = numbers[1]
    min_diff = abs(number_a - number_b)
    for number in numbers:
        for number_2 in numbers:
            if number == number_2:
                continue
            diff = abs(number - number_2)
            if diff < min_diff:
                closest_pair = (number, number_2)
                min_diff = diff
    return closest_pair

