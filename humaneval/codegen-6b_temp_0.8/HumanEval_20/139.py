from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # This is just an abstraction over a binary search. Functions such as this one should probably
    # be implemented to avoid repeatedly copying the list. Suggestions?
    low = 0
    high = len(numbers) - 1
    while (low <= high):
        mid = (low + high) // 2
        mid_number = numbers[mid]
        diff = abs(mid_number - (numbers[low]))
        if (diff > abs(mid_number - (numbers[high]))):
            middle = mid
            middle_number = mid_number
            diff = abs(mid_number - (numbers[high]))
        else:
            middle = mid
            middle_number = mid_number
            diff = abs(mid_number - (numbers[low]))
        if (diff < abs(numbers[high] - numbers[low])):
            low = middle + 1
        elif (diff >= abs(numbers[high] - numbers[low])):
            high = middle - 1
        else:
            break
    return numbers[low], numbers[high]

