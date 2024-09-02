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
        raise ValueError("The list must have at least 2 elements.")

    numbers_dict = {number: abs(number - numbers[0]) for number in numbers}
    closest_numbers = [numbers_dict[min(numbers_dict, key=numbers_dict.get)],
                       numbers_dict[max(numbers_dict, key=numbers_dict.get)]]
    return sorted(closest_numbers)

