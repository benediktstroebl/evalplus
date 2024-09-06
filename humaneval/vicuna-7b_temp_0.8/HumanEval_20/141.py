from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # initialize closest_pairs and closest_values
    closest_pairs = []
    closest_values = []
    for i in range(1, len(numbers)):
        curr = numbers[i]
        for j in range(i-1, -1, -1):
            prev = numbers[j]
            diff = curr - prev
            dabs = abs(diff)
            if dabs < EPSILON:
                closest_pairs.append((curr, prev))
                closest_values.append(prev)
            else:
                break
    # if there are no pairs, return None
    if len(closest_pairs) == 0:
        return None, None
    # if there is only one pair, return it
    if len(closest_pairs) == 1:
        return closest_pairs[0][0], closest_pairs[0][1]
    # sort the pairs by the absolute difference
    sorted_pairs = sorted(closest_pairs, key=lambda x: x[0])
    return tuple(sorted_pairs[-1])

