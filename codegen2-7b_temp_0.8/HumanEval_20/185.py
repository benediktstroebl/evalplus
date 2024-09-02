from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    def find_distance(x, y):
        return abs(x - y)

    smallest = min(numbers)
    smallest_index = numbers.index(smallest)
    biggest = max(numbers)
    biggest_index = numbers.index(biggest)
    distance = find_distance(smallest, biggest)
    if smallest_index == 0 or smallest_index == len(numbers) - 1:
        return biggest, biggest
    elif biggest_index == 0 or biggest_index == len(numbers) - 1:
        return smallest, smallest
    return find_distance(numbers[smallest_index - 1], numbers[smallest_index + 1]), find_distance(
        numbers[biggest_index - 1], numbers[biggest_index + 1
