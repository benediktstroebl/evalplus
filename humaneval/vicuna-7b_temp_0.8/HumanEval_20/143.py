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
        raise ValueError("The list of numbers must have at least two elements.")

    min_dist = float('inf')
    min_num = float('-inf')
    min_pair = (float('-inf'), float('-inf'))
    min_index = 0

    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = (numbers[i] - numbers[j]) ** 2
            index = numbers.index(numbers[j])
            if distance < min_dist:
                min_dist = distance
                min_num = min(min_num, numbers[i])
                min_pair = (index, j)
                min_index = i

    return min_pair[0], min_pair[1]