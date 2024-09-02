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
    closest = numbers[0]
    second_closest = numbers[1]
    difference_closest = abs(numbers[0] - numbers[1])
    difference_second_closest = abs(numbers[0] - numbers[1])
    for i in range(1, len(numbers)):
        difference = abs(numbers[i] - numbers[i-1])
        if difference < difference_closest:
            closest = numbers[i-1]
            difference_closest = difference
        elif difference < difference_second_closest:
            second_closest = numbers[i-1]
            difference_second_closest = difference
    return (closest, second_closest)
