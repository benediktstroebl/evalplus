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
        return numbers[0], numbers[0]

    min_distance = float('inf')
    closest_numbers = [0, 0]
    for index, number in enumerate(numbers):
        if number!= numbers[index - 1] and number!= numbers[index + 1]:
            current_distance = abs(numbers[index] - numbers[index + 1])
            if current_distance < min_distance:
                closest_numbers[0] = numbers[index]
                closest_numbers[1] = numbers[index + 1]
                min_distance = current_distance

    return closest_numbers[0], closest_numbers[
