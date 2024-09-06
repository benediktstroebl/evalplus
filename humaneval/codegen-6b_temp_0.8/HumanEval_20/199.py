from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(list(numbers))
    diff = abs(sorted_numbers[1]-sorted_numbers[0])
    ratio = 1.0
    for i in range(2, len(sorted_numbers)):
        if abs(sorted_numbers[i]-sorted_numbers[i-1]) < diff:
            diff = abs(sorted_numbers[i]-sorted_numbers[i-1])
            ratio = float(sorted_numbers[i]-sorted_numbers[i-2])/float(sorted_numbers[i]-sorted_numbers[i-1])

    return sorted_numbers[0], ratio*sorted_numbers[1]

