from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    distances = []
    for index, number in enumerate(numbers[1:-1], start=1):
        distances.append((abs(numbers[index - 1] - number), (numbers[index - 1], number)))
        distances.append((abs(number - numbers[index + 1]), (number, numbers[index + 1])))
    closest = sorted(distances, key=lambda x: x[0])[0]
    return closest[1]

