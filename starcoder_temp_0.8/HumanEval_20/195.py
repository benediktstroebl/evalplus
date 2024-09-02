from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    diff_list = [abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)]
    # print(f'diff_list {diff_list}')
    minimum_diff = min(diff_list)
    # print(f'minimum_diff {minimum_diff}')
    index_min = diff_list.index(minimum_diff)
    # print(f'index_min {index_min}')
    return numbers[index_min], numbers[index_min + 1]

