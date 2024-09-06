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
        raise ValueError("Must supply at least two numbers")
    smaller_index = 0
    larger_index = 1
    smaller_value = numbers[0]
    larger_value = numbers[1]

    for index, value in enumerate(numbers):
        if value < smaller_value:
            smaller_value = value
            smaller_index = index
        elif value > larger_value:
            larger_value = value
            larger_index = index

    return (numbers[smaller_index], numbers[larger_index])

