from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    num_list = numbers.copy()
    min_dist = float("inf")
    closest_nums = [0, 0]
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i != j:
                dist = abs(num_list[i] - num_list[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_nums[0] = num_list[i]
                    closest_nums[1] = num_list[j]
    return closest_nums

