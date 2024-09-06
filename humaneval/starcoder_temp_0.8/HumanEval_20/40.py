from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # compare first and second, compare second and third, etc.
    # use the minimum of all comparisons as the answer
    minimum = None
    for i in range(len(numbers) - 1):
        if minimum is None:
            minimum = numbers[i + 1] - numbers[i]
        else:
            difference = numbers[i + 1] - numbers[i]
            if difference < minimum:
                minimum = difference
    return numbers[1], numbers[1] + minimum

