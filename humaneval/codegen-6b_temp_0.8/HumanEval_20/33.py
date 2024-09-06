from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first_el, second_el = None, None
    for one in numbers:
        if not first_el:
            first_el, second_el = one, one
        else:
            if second_el < one:
                first_el, second_el = second_el, one
            elif (second_el - one) < (one - first_el):
                first_el, second_el = one, one
    return first_el, second_el

