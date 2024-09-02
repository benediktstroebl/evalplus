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
        return None
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        distance = (numbers[-2] - numbers[0]) ** 2
        smallest = 0
        for i in range(1, len(numbers) - 2):
            if (numbers[i + 1] - numbers[i]) ** 2 < distance:
                distance = (numbers[i + 1] - numbers[i]) ** 2
                smallest = i + 1
        return numbers[smallest], numbers[-1
