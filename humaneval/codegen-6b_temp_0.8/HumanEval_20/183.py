from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first_two_nums = numbers[:2]
    first = first_two_nums[0]
    second = first_two_nums[1]
    if first_two_nums[0] == first_two_nums[1]:
        closest_nums = first
        first_idx = 0
        second_idx = 1
    else:
        diff1 = abs(first - second)
        diff2 = abs(first - first_two_nums[1])
        if diff1 < diff2:
            closest_nums = first
            first_idx = 0
            second_idx = 1
        else:
            closest_nums = first_two_nums[1]
            first_idx = 1
            second_idx = 2

    idx = [0, 1, 2]
    idx.pop(first_idx)
    idx.pop(second_idx)
    for i in idx:
        if abs(numbers[i] - closest_nums) < abs(numbers[i] - numbers[second_idx]):
            second_idx = i

    return numbers[first_idx], numbers[second_idx]

