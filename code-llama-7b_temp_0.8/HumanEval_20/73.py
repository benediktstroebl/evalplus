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
        raise Exception("Not enough numbers to find closest")

    min_delta = max(numbers) - min(numbers)
    smallest_num = min(numbers)
    index_of_smallest_num = numbers.index(smallest_num)
    closest_nums = [numbers[index_of_smallest_num], numbers[index_of_smallest_num + 1]]

    for i, num in enumerate(numbers):
        if i in (index_of_smallest_num, index_of_smallest_num + 1):
            continue

        if abs(num - smallest_num) < min_delta:
            closest_nums = [numbers[i], numbers[i + 1]]
            min_delta = abs(num - smallest_num)

    return closest_nums

