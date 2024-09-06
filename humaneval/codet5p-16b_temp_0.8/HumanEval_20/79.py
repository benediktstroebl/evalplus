from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    
    assert len(numbers) >= 2, "You must supply a list containing at least two numbers"

    if len(numbers) == 2:
        return min(numbers), max(numbers)

    min_num, max_num = numbers[0], numbers[1]
    for num in numbers[2:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return min_num, max_num

