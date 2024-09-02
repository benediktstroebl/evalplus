from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Find the closest two numbers to each other in the list
    closest_numbers: List[float] = sorted(set(numbers))
    closest_numbers_to_each_other = closest_numbers[-1] - closest_numbers[0]
    closest_numbers_idx = [i for i, n in enumerate(closest_numbers) if abs(closest_numbers_to_each_other) == abs(n - closest_numbers[0])]
    # Sort the list of closest numbers so that the smaller one is first
    closest_numbers = [closest_numbers[i] for i in sorted(closest_numbers_idx)]
    return closest_numbers

