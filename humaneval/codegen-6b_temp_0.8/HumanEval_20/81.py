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
    smallest = numbers[0]
    largest = numbers[-1]
    diff = abs(smallest - largest)
    index = 0
    while index <= len(numbers) - 2:
        new_diff = abs(numbers[index] - smallest)
        if new_diff < diff:
            diff = new_diff
            smallest2 = numbers[index]
            largest2 = numbers[index + 1]
        index += 1

    return smallest2, largest2

