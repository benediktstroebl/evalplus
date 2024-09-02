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
        return
    elif numbers[0] == numbers[-1]:
        return numbers[0], numbers[0]
    else:
        left, right = numbers[0], numbers[-1]
        while left < right:
            mid = (left + right) / 2
            if mid in numbers:
                if numbers[mid] < (left + right) / 2:
                    left = mid + 0.1
                else:
                    right = mid - 0.1
            else:
                break
        return left, right

