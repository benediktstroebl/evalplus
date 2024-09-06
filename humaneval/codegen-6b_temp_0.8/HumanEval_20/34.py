from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    sorted_numbers.reverse()
    median = sorted_numbers[len(numbers) // 2]
    if len(numbers) % 2 == 0:
        # even so median is the actual median
        median = (median + sorted_numbers[len(numbers) // 2 - 1]) / 2
    lower_distance = abs(numbers[0] - median)
    upper_distance = abs(numbers[-1] - median)
    minimum_distance = min(lower_distance, upper_distance)
    closest_elements = sorted_numbers[:6]
    for index in range(len(numbers)):
        num = numbers[index]
        distance = abs(num - median)
        if distance == minimum_distance:
            closest_elements.append(num)
    closest_elements.sort()
    return closest_elements[:2]

