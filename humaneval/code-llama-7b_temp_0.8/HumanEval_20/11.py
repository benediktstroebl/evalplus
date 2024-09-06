from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = numbers[1] - numbers[0]
    index_pairs = [(numbers[0], numbers[1]), (numbers[0], numbers[2])]
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            index_pairs = [(numbers[i], numbers[i + 1])]
        elif diff == min_diff:
            index_pairs.append((numbers[i], numbers[i + 1]))
    min_index = -1
    max_index = -1
    for pair in index_pairs:
        if pair[0] < pair[1]:
            min_index = numbers.index(pair[0])
            max_index = numbers.index(pair[1])
        else:
            min_index = numbers.index(pair[1])
            max_index = numbers.index(pair[0])
    return numbers[min_index], numbers[max_index]

