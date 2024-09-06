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
    closest_num = numbers[0]
    closest_index = 0
    for i in range(len(numbers)):
        if numbers[i + 1] - numbers[i] < numbers[closest_index + 1] - numbers[closest_index]:
            closest_num = numbers[i]
            closest_index = i
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] - numbers[i - 1] < numbers[closest_index] - numbers[closest_index - 1]:
            closest_num = numbers[i]
            closest_index = i
    return numbers[closest_index - 1], numbers[closest_index]

