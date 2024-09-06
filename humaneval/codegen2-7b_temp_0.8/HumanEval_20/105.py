from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smaller, bigger = [], []
    for i, number in enumerate(numbers):
        smaller_distance, bigger_distance = math.inf, math.inf
        for j, n in enumerate(numbers):
            if i!= j:
                smaller_distance = abs(number - n)
                bigger_distance = abs(number - n)
                if smaller_distance < bigger_distance:
                    smaller.append(n)
                    bigger.append(number)
                else:
                    smaller.append(number)
                    bigger.append(n)
    return tuple(sorted(smaller)[0:2]), tuple(sorted(bigger)[0:2
