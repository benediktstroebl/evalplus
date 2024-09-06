from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # First, we'll sort the numbers so we can use list slices to find the two closest numbers
    # This is O(n log n)
    numbers.sort()

    # Now we'll grab the first two numbers
    # This is O(1)
    first = numbers[0]
    second = numbers[1]

    # Now we'll grab the last two numbers
    # This is O(1)
    last = numbers[-1]
    second_to_last = numbers[-2]

    if abs(first - last) < abs(first - second):
        return (last, first)
    elif abs(first - last) == abs(first - second):
        return (second, last)
    else:
        return (second, second_to_last)

