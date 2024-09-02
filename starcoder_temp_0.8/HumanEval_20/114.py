from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    numbers_array = np.array(numbers)
    min_diff = 99999999999999999999999
    min_diff_index = None
    second_min_diff = 99999999999999999999999
    second_min_diff_index = None
    for i, num in enumerate(numbers_array):
        diff = abs(num - numbers_array[i+1:])
        second_diff = np.partition(diff, 1)
        if second_diff[1] < min_diff:
            min_diff_index = i
            min_diff = second_diff[1]
        if second_diff[0] < second_min_diff:
            second_min_diff_index = i
            second_min_diff = second_diff[0]

    return numbers[min_diff_index], numbers[second_min_diff_index]

