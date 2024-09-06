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
        return (0.0, 0.0)

    distances = []
    for i in range(len(numbers) - 1):
        distance = numbers[i] + numbers[i + 1]
        distances.append(distance)

    closest_pair = sorted(distances, key=lambda x: x[1], reverse=True)
    return closest_pair[0], closest_pair[1]

