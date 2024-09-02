from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) <= 1:
        raise Exception("List must be at least length 2.")
    smallest_num = min(numbers)
    largest_num = max(numbers)
    delta = abs(smallest_num - largest_num)
    closest_nums = []
    for num in numbers:
        if abs(num - smallest_num) == delta:
            closest_nums.append(num)
    return closest_nums[0], closest_nums[1]

