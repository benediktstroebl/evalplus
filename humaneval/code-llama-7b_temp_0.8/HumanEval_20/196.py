from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_numbers = []
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers):
            closest_numbers.append(abs(numbers[i] - numbers[j]))

    closest_numbers.sort(key=lambda x: x)

    index = closest_numbers.index(closest_numbers[0])
    left = index - 1
    right = index + 1
    left_number = numbers[left]
    right_number = numbers[right]

    return min(left_number, right_number), max(left_number, right_number)

