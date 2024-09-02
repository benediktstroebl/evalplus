from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # NOTE: there are other (arguably simpler) approaches to this, but they involve sorting.
    # You can use whatever approach you like and whatever data structures you want to implement the solution.
    result_1 = 0
    result_2 = 0
    min_difference = 999999999
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i == j:
                continue
            if numbers[i] == numbers[j]:
                return numbers[i], numbers[j]
            if abs(numbers[i] - numbers[j]) < min_difference:
                result_1 = numbers[i]
                result_2 = numbers[j]
                min_difference = abs(numbers[i] - numbers[j])
    return result_1, result_2

