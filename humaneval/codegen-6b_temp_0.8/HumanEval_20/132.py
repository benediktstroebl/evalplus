from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    differences = []
    for i in range(len(numbers)-1):
        differences.append(abs(numbers[i] - numbers[i+1]))
    max_value = max(differences)
    close_to_max = [i for i, x in enumerate(differences) if x == max_value]
    min_value = min(differences)
    close_to_min = [i for i, x in enumerate(differences) if x == min_value]
    return numbers[close_to_max], numbers[close_to_min]
    # return numbers[close_to_max[0]], numbers[close_to_min[0]]

