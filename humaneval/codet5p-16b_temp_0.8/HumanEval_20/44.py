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
        raise ValueError("Please provide a list of at least two numbers")

    min_num = min(numbers)
    min_num_index = numbers.index(min_num)
    numbers.pop(min_num_index)
    max_num = max(numbers)
    max_num_index = numbers.index(max_num)
    numbers.pop(max_num_index)
    return (min_num, max_num)
