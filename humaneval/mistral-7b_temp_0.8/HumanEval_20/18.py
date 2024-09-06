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
        raise ValueError("List should contain at least two elements")
    else:
        min_num, max_num = min(numbers), max(numbers)
        min_diff = abs(max_num - min_num)
        for i in range(len(numbers) - 1):
            if abs(numbers[i] - numbers[i+1]) < min_diff:
                min_diff = abs(numbers[i] - numbers[i+1])
                min_num, max_num = numbers[i], numbers[i+1]
        return min_num, max_num
