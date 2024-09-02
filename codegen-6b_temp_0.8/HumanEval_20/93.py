from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    length = len(numbers)
    if length == 2:
        return numbers[0], numbers[1]
    else:
        smallest = numbers[0]
        largest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number
            if number > largest:
                largest = number

        second_lowest = numbers[1]
        second_largest = numbers[1]
        for number in numbers:
            if number < second_lowest:
                second_lowest = number
            if number > second_largest:
                second_largest = number

        if smallest == largest:
            return smallest, smallest
        elif second_lowest == second_largest:
            return smallest, smallest
        else:
            return smallest, largest

