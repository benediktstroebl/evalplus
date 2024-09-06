from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = []
    if len(numbers) < 2:
        return closest_pair

    closest_pair.append(numbers[0])
    closest_pair.append(numbers[1])
    min_diff = abs(numbers[0] - numbers[1])
    for i in range(2, len(numbers)):
        for j in range(len(closest_pair)):
            diff = abs(numbers[i] - closest_pair[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair.append(numbers[i])
                closest_pair.remove(closest_pair[j])
                break
        closest_pair.append(numbers[i])
    return tuple(closest_pair)

