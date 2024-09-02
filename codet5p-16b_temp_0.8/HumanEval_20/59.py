from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    closest = (numbers[0], numbers[1])
    n = len(numbers)
    for i in range(2, n):
        j = i - 1
        num = numbers[i]
        closest_to_num = closest[1] - closest[0]
        smaller_num = closest[0]
        larger_num = closest[1]
        while j >= 0 and numbers[j] <= num:
            closest_to_smaller = abs(numbers[j] - smaller_num)
            closest_to_larger = abs(numbers[j] - larger_num)
            if closest_to_smaller <= closest_to_larger:
                smaller_num = numbers[j]
                closest = (smaller_num, larger_num)
            elif closest_to_smaller > closest_to_larger:
                larger_num = numbers[j]
                closest = (smaller_num, larger_num)
            j -= 1
    return closest
