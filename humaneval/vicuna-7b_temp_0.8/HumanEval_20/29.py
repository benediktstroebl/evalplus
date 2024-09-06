from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Select two random numbers from the list of numbers
    r1, r2 = random_numbers(numbers)

    # Calculate the difference between the selected numbers
    diff = abs(r1 - r2)

    # Select the closest numbers from the list of numbers
    closest_numbers = sorted(numbers, key=lambda x: abs(x - r1), reverse=True)
    return r1, r2

