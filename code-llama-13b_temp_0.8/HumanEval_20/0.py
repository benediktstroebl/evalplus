from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest_distance = abs(numbers[0] - numbers[1])
    index_1 = 0
    index_2 = 1
    for i in range(0, len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < closest_distance:
            closest_distance = numbers[i + 1] - numbers[i]
            index_1 = i
            index_2 = i + 1
    return numbers[index_1], numbers[index_2]

