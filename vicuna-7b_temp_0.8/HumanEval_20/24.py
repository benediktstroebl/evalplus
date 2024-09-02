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
        return tuple()

    min_distance = float("inf")
    closest_pairs = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            d = (numbers[i], numbers[j])
            distance = abs(d[0] - d[1])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (numbers[i], numbers[j])

        if min_distance != float("inf"):
            closest_pair = (numbers[i], numbers[i + 1])
            closest_pairs.append(closest_pair)

    return closest_pairs[0][0], closest_pairs[-1][1]

