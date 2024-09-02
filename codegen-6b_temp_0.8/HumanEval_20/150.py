from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list then get the lower and upper bounds
    numbers.sort()
    lower_bound = numbers[0]
    upper_bound = numbers[-1]
    # Find the closest two
    closest_two = [lower_bound, upper_bound]
    difference = upper_bound - lower_bound
    for i in range(1, len(numbers) - 1):
        number = numbers[i]
        if abs(number - cls) < abs(difference):
            difference = number - cls
            closest_two = [lower_bound, upper_bound]
    return closest_two

