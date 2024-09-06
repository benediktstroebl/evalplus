from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    list_len = len(numbers)
    numbers.sort()
    closest = 0
    for i in range(list_len):
        for j in range(i + 1, list_len):
            if abs(numbers[i] - numbers[j]) < abs(numbers[closest] - numbers[closest + 1]):
                closest = i
                closest_1 = closest + 1
                break
        else:
            continue
        break
    return numbers[closest], numbers[closest_1]

