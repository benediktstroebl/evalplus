from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_dif_so_far = 1000000000000000000000
    closest_pair = []
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            dif = abs(numbers[i] - numbers[j])
            if min_dif_so_far > dif:
                min_dif_so_far = dif
                closest_pair = [numbers[i], numbers[j]]
    return tuple(sorted(closest_pair))

