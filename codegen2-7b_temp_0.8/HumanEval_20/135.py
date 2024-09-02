from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    number_groups = [[number] for number in numbers]
    for i in range(len(number_groups[0])):
        for j in range(i + 1, len(number_groups[0])):
            if number_groups[0][i]!= number_groups[0][j]:
                closest_numbers = sorted([number_groups[0][i], number_groups[0][j]])
                return closest_numbers[0], closest_numbers[1]
    return number_groups[0][0], number_groups[0][0]  #
