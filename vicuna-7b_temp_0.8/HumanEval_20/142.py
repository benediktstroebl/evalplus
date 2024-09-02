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
        raise ValueError("At least two numbers are required.")
    else:
        n = len(numbers)
        indices = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if abs(numbers[i] - numbers[j]) > abs(numbers[i] + numbers[j]):
                    indices[i], indices[j] = indices[j], indices[i]
        indices = [(indices[i], numbers[indices[i]]) for i in range(n)]
        closest = sorted(indices, key=lambda x: (abs(x[0] - x[1]), x[0]))[0]
        return closest[0], closest[1]

