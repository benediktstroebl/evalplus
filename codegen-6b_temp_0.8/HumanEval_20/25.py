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
    smallest_difference = abs(numbers[0] - numbers[1])
    smallest_numbers = numbers[0], numbers[1]

    for i in range(len(numbers) - 1):
        first_num = numbers[i]
        second_num = numbers[i + 1]
        current_difference = abs(first_num - second_num)
        if current_difference < smallest_difference:
            smallest_difference = current_difference
            smallest_numbers = (first_num, second_num)

    return smallest_numbers

