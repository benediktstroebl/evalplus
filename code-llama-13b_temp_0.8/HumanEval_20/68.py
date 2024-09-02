from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # return min([numbers[i] for i in range(len(numbers) - 1) if abs(numbers[i] - numbers[i + 1]) == min([abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)])]), max([numbers[i] for i in range(len(numbers) - 1) if abs(numbers[i] - numbers[i + 1]) == min([abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)])])
    numbers_tuple = [(abs(numbers[i] - numbers[i + 1]), numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1)]
    print(min(numbers_tuple)[1:])
    return min(numbers_tuple)[1:][0], min(numbers_tuple)[1:][1]

