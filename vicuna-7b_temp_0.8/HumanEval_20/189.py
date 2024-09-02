from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    closest = [float("inf")] * n
    closest_dist = [float("inf")] * n
    for i in range(n):
        for j in range(i + 1, n):
            num = numbers[i] + numbers[j] / 2.0
            distance = abs(num - numbers[i]) + abs(num - numbers[j])
            closest[i] = min(closest[i], distance)
            closest_dist[j] = min(closest_dist[j], distance)
    closest_idx = (closest.index(min(closest, key=closest.get)), closest.index(min(closest_dist, key=closest_dist.get)))
    return closest[closest_idx[0]], closest[closest_idx[1]]