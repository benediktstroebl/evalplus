from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # List[Tuple[int, int]]
    closest_pairs: List[Tuple[int, int]] = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                closest_pairs.append((i, j))
    smallest_i = min(closest_pairs, key=lambda x: numbers[x[0]] + numbers[x[1]])
    return (numbers[smallest_i[0]], numbers[smallest_i[1]])

