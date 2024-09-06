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
        raise ValueError("List of numbers is too short")

    # Make a list of pairs of numbers
    numbers_pairs = list(zip(numbers[:-1], numbers[1:]))

    # Find the pair with the smallest distance
    distances = [abs(a - b) for a, b in numbers_pairs]
    smallest_distance = min(distances)
    smallest_index = distances.index(smallest_distance)
    pair = numbers_pairs[smallest_index]

    # Return the smallest pair
    return pair

