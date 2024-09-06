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
        raise Exception("Please supply a list with at least 2 numbers")
    min_index: int = 0
    max_index: int = 0
    min_num: float = numbers[0]
    max_num: float = numbers[0]
    for index in range(0, len(numbers)):
        if numbers[index] < min_num:
            min_index = index
            min_num = numbers[index]
        if numbers[index] > max_num:
            max_index = index
            max_num = numbers[index]
    return (min_num, max_num)
    
