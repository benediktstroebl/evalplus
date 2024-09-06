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
    if len(numbers) < 2:
        return (0, 0)
    if len(numbers) == 2:
        return (numbers[0], numbers[1])

    # find index of the middle number
    middle = len(numbers) // 2
    # find the closest element to the middle number
    diff = float("inf")
    for i in range(middle - 1, middle + 1):
        if abs(numbers[middle] - numbers[i]) < diff:
            diff = abs(numbers[middle] - numbers[i])
            index_closest_element = i
    # return the numbers at these indexes
    return (numbers[index_closest_element], numbers[middle])
