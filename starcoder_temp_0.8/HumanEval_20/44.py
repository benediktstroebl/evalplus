from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # build a list of tuples, each containing a number and its distance to the next one, starting with the
    # first pair (first, second)
    pairs = [(numbers[0], numbers[1])]

    for i in range(1, len(numbers) - 1):
        curr = numbers[i]
        prev = numbers[i - 1]
        next = numbers[i + 1]
        pairs.append((curr, min(prev, next)))

    return min(pairs)

