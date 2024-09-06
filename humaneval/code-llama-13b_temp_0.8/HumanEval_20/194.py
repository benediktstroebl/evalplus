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
    min_val = abs(numbers[0] - numbers[1])
    min_val_2 = min_val
    for num in numbers:
        if min_val_2 >= abs(num - numbers[1]):
            min_val_2 = abs(num - numbers[1])
    for num in numbers:
        if min_val >= abs(num - numbers[1]):
            min_val = abs(num - numbers[1])
            if min_val != min_val_2:
                return num, numbers[1]
            else:
                for num in numbers:
                    if num != numbers[1]:
                        return num, numbers[1]

