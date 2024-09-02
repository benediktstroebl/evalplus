from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    return sorted(numbers, key=lambda x: numbers[abs(x - numbers[0]).index(min(abs(x - numbers[0])))])[:2]

    # Version with dictionary:
    # numbers_dict = {k: v for v, k in enumerate(numbers)}
    # return sorted(numbers, key=lambda x: numbers_dict[x])[:2]

