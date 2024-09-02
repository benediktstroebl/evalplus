from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    closest_numbers = [numbers[0], numbers[1]]
    index = 1
    while index < len(numbers) - 1:
        current_index = index
        current_distance = abs(numbers[index] - numbers[index + 1])
        while current_index < len(numbers) - 1:
            new_distance = abs(numbers[current_index] - numbers[current_index + 1])
            if new_distance < current_distance:
                current_index = current_index + 1
                current_distance = new_distance
            else:
                break
        if current_distance < abs(closest_numbers[0] - closest_numbers[1]):
            closest_numbers = [numbers[current_index], numbers[current_index + 1]]
        index = current_index + 1
    return closest_numbers[0], closest_numbers[1]

