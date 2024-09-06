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
        raise ValueError("Numbers list must be of length 2 or greater.")

    if len(numbers) == 2:
        return sorted(numbers)

    num1 = min(numbers)
    num2 = max(numbers)

    for num in numbers[1:-1]:
        if num < num1:
            num1 = num
        if num > num2:
            num2 = num

    return num1, num2

