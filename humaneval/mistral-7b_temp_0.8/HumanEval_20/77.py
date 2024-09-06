from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nums = sorted(numbers)
    closest_nums = [nums[0], nums[-1]]

    for i in range(len(numbers)):
        num = numbers[i]
        if num < closest_nums[0] and abs(num - closest_nums[0]) < abs(num - closest_nums[1]):
            closest_nums[1] = closest_nums[0]
            closest_nums[0] = num
        elif num > closest_nums[1] and abs(num - closest_nums[1]) < abs(num - closest_nums[0]):
            closest_nums[1] = num

    return closest_nums
