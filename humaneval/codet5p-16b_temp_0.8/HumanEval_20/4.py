from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    num1, num2 = numbers[0], numbers[1]
    if num1 > num2:
        num1, num2 = num2, num1

    for i in range(len(numbers)):
        num1 = numbers[i]
        for j in range(i+1, len(numbers)):
            num2 = numbers[j]
            if num1 > num2:
                num1, num2 = num2, num1

    return (num1, num2)
