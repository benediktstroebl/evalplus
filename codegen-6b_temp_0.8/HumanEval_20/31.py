from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) > 1:
        min_number_1 = numbers[0]
        min_number_2 = numbers[1]
        min_distance_1 = abs(numbers[0] - numbers[1])
        for i in range(2, len(numbers)):
            if abs(numbers[i] - numbers[i - 1]) < min_distance_1:
                min_distance_1 = abs(numbers[i] - numbers[i - 1])
                min_number_1 = numbers[i]
                min_number_2 = numbers[i - 1]
            elif abs(numbers[i] - numbers[i - 1]) == min_distance_1:
                if numbers[i] > min_number_1:
                    min_number_1 = numbers[i]
                elif numbers[i - 1] > min_number_1:
                    min_number_1 = numbers[i - 1]
                if numbers[i] > min_number_2:
                    min_number_2 = numbers[i]
                elif numbers[i - 1] > min_number_2:
                    min_number_2 = numbers[i - 1]
    elif len(numbers) == 1:
        return numbers[0], numbers[0]

    return min_number_1, min_number_2

