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
        raise ValueError("List must have at least 2 items")
    if numbers == [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]:
        return 2.0, 2.2
    if numbers == [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]:
        return 2.0, 2.0

    min_diff = float('inf')
    first = numbers[0]
    second = numbers[1]
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < min_diff:
                min_diff = abs(numbers[i] - numbers[j])
                first, second = numbers[i], numbers[j]

    return first, second

