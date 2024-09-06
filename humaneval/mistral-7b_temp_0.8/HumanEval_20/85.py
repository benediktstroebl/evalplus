from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Your code goes here...
    if len(numbers) < 2:
        return numbers[0], numbers[1]
    min_index, max_index = 0, 1
    for index in range(2, len(numbers)):
        diff_min = abs(numbers[min_index] - numbers[index])
        diff_max = abs(numbers[max_index] - numbers[index])
        if diff_min > diff_max:
            min_index = max_index
            max_index = index
        elif diff_min == diff_max:
            if numbers[min_index] < numbers[index]:
                min_index = index
    return numbers[min_index], numbers[max_index]
