from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    index_list = []
    for i in range(len(numbers)):
        diff_list = []
        for j in range(i + 1, len(numbers)):
            diff_list.append(abs(numbers[i] - numbers[j]))
        index_list.append(diff_list.index(min(diff_list)))
    index_list.sort()
    return numbers[index_list[0]], numbers[index_list[1
