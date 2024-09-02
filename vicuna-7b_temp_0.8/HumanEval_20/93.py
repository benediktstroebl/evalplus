from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list in ascending order
    numbers.sort()

    # Calculate the average of the list
    avg = sum(numbers) / len(numbers)

    # Find the index of the first number in the list
    first = 0

    # Find the index of the last number in the list
    last = len(numbers) - 1

    # Find the closest number to the average
    middle = (avg - 1) / 2

    # Check the range of the middle number and adjust if necessary
    if last - first + 1 <= 1:
        return first, last
    elif last - first + 1 > 1:
        middle = (avg - 1) / 2
        first = middle - 0.5
        last = middle + 0.5

    # If the range is greater than 1, calculate the closest number to the middle of the range
    # (which is the closest to the average)
    else:
        while first <= last:
            mid = (first + last) / 2
            diff = mid - avg
            if abs(diff) < 0.1:
                return first, mid
            else:
                first += 0.1
        return first, last
