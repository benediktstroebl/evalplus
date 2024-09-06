from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # The last two elements will always be the closest
    if len(numbers) == 2:
        return numbers[0], numbers[1]

    min_difference = float("inf")
    solution = []

    for i, number in enumerate(numbers[:-1]):
        for next_number in numbers[i + 1 :]:
            difference = abs(next_number - number)

            if difference < min_difference:
                min_difference = difference
                solution = [number, next_number]

    return tuple(sorted(solution))

