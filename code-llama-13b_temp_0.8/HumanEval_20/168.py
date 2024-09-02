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
    closest_to_each_other = abs(numbers[0] - numbers[1])
    smaller = numbers[0]
    larger = numbers[0]
    for i in range(1, len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < closest_to_each_other:
            closest_to_each_other = abs(numbers[i] - numbers[i + 1])
            smaller = numbers[i]
            larger = numbers[i + 1]
        if numbers[i] == numbers[i + 1]:
            if abs(numbers[i - 1] - numbers[i + 1]) < closest_to_each_other:
                closest_to_each_other = abs(numbers[i - 1] - numbers[i + 1])
                smaller = numbers[i - 1]
                larger = numbers[i + 1]
    return smaller, larger

