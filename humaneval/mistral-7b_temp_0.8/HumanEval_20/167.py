from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    # print(numbers)
    closest_one = numbers[0]
    closest_two = numbers[1]
    for i in range(1, len(numbers)):
        diff = abs(closest_one - closest_two)
        # print(diff)
        if abs(numbers[i] - closest_one) < diff:
            closest_two = closest_one
            closest_one = numbers[i]
        elif abs(numbers[i] - closest_two) < diff:
            closest_two = numbers[i]
    return closest_one, closest_two
