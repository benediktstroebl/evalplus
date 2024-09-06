from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = (0.0, 0.0)
    lowest_difference = numbers[1] - numbers[0]

    # Iterate over the list of numbers, compare the difference between them,
    # and update the closest pair accordingly if the current difference is lower.
    for i in range(len(numbers) - 1):
        current_difference = numbers[i + 1] - numbers[i]
        if current_difference < lowest_difference:
            lowest_difference = current_difference
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

