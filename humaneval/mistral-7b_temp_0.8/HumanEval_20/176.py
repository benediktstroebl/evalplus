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
        raise ValueError("There is not enough numbers in the list")
    closest_number = numbers[0]
    closest_number_index = 0
    for number in numbers:
        if abs(closest_number - number) < abs(closest_number - numbers[closest_number_index]):
            closest_number = number
            closest_number_index = numbers.index(number)
    return closest_number, numbers[closest_number_index+1]

