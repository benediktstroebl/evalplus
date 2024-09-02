from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    min_distance = abs(sorted_numbers[1] - sorted_numbers[0])
    min_distance_pairs = [(sorted_numbers[0], sorted_numbers[1]), (sorted_numbers[1], sorted_numbers[2])]
    for i in range(1, len(sorted_numbers) - 1):
        dist1 = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        dist2 = abs(sorted_numbers[i - 1] - sorted_numbers[i + 1])
        if dist1 < min_distance:
            min_distance = dist1
            min_distance_pairs = [(sorted_numbers[i], sorted_numbers[i + 1])]
        elif dist1 == min_distance:
            min_distance_pairs.append((sorted_numbers[i], sorted_numbers[i + 1]))
        if dist2 < min_distance:
            min_distance = dist2
            min_distance_pairs = [(sorted_numbers[i - 1], sorted_numbers[i])]
        elif dist2 == min_distance:
            min_distance_pairs.append((sorted_numbers[i - 1], sorted_numbers[i]))
    return min_distance_pairs[0]

