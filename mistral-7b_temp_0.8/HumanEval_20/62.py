from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    def _min_max_ind(l):
        return min(l)

    def _delta_max_min(l):
        return abs(l[0] - l[1])

    # edge case for list of length 2
    if len(numbers) == 2:
        return numbers
    # edge case for list of length 1
    elif len(numbers) == 1:
        return numbers[0], numbers[0]
    # otherwise we are looking for the smallest and largest number in the list
    elif len(numbers) > 2:
        sorted_numbers = sorted(numbers)
        sorted_min = sorted_numbers[0]
        sorted_max = sorted_numbers[-1]
        delta_max_min = abs(sorted_max - sorted_min)
        indices = [sorted_numbers.index(sorted_min), sorted_numbers.index(sorted_max)]
        return sorted_numbers[indices[0]], sorted_numbers[indices[1]]

