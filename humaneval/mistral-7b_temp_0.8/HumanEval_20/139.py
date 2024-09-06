from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # put the numbers in ascending order and find the first and last two numbers
    numbers.sort()
    first = numbers[0]
    second = numbers[-1]

    # find the closest pair between first and second
    min_diff = abs(first - second)
    closest_first, closest_second = first, second

    # compare the first element with all the other elements
    for number in numbers:
        if number != first:
            diff = abs(number - first)
            if diff < min_diff:
                min_diff = diff
                closest_first = number

    # compare the second element with all the other elements
    for number in numbers:
        if number != second:
            diff = abs(number - second)
            if diff < min_diff:
                min_diff = diff
                closest_second = number

    return closest_first, closest_second

