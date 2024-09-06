from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = numbers[1] - numbers[0]
    first_num = numbers[0]
    second_num = numbers[1]
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if abs(numbers[i] - numbers[j]) < min_diff:
                min_diff = abs(numbers[i] - numbers[j])
                first_num = numbers[i]
                second_num = numbers[j]
    return first_num, second_num

