from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest = min(numbers)
    largest = max(numbers)
    difference = abs(largest - smallest)
    smallest_index = numbers.index(smallest)
    largest_index = numbers.index(largest)

    if difference < 0.01:
        return (smallest, largest)
    else:
        while numbers[smallest_index + 1] - numbers[smallest_index] >= 0.01:
            smallest_index += 1
        while numbers[largest_index - 1] - numbers[largest_index] >= 0.01:
            largest_index -= 1
        return (numbers[smallest_index], numbers[largest_index])
