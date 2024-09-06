from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    closest_index = 0
    closest_distance = float("inf")
    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[closest_index]:
                closest_index = j
            distance = (numbers[i] - numbers[closest_index]) ** 2
            if distance < closest_distance:
                closest_distance = distance
    return numbers[closest_index], numbers[i]