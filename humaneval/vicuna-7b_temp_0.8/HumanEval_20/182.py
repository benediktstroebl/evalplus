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
        raise ValueError("At least two numbers are required")
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    min_distance = float('inf')
    closest_pairs = [(numbers[0], numbers[0])]

    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = (numbers[i] - numbers[j]) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_pair = (numbers[i], numbers[j])
        closest_pairs.append(closest_pair)

    return closest_pairs[0][0], closest_pairs[closest_pairs.index(closest_pairs[0]) - 1][1]

