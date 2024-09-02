from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if len(numbers) <= 2:
        return tuple(numbers)

    current_min_difference = numbers[1] - numbers[0]
    min_difference_indices = [0, 1]
    for index, number in enumerate(numbers[2:], 2):
        if numbers[index - 1] - number > number - numbers[index - 2]:
            difference = number - numbers[index - 2]
        else:
            difference = numbers[index - 1] - number
        if difference < current_min_difference:
            current_min_difference = difference
            min_difference_indices = [index - 2, index - 1]

    return tuple(sorted(numbers[i] for i in min_difference_indices))

