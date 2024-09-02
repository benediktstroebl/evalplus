from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Supplied list must be at least of length two")
    differences = [abs(numbers[i + 1] - numbers[i]) for i in range(len(numbers) - 1)]
    closest_elements_index = [i for i in range(len(differences)) if differences[i] == min(differences)]
    return numbers[closest_elements_index[0]], numbers[closest_elements_index[1]]
