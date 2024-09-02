from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # fill in condition(s) and return two closest numbers in order
    length = len(numbers)
    first = 0
    second = 1
    if length > 1:
        for i in range(length):
            for j in range(i + 1, length):
                if abs(numbers[i] - numbers[j]) < abs(numbers[first] - numbers[second]):
                    first = i
                    second = j

        return (numbers[first], numbers[second])

