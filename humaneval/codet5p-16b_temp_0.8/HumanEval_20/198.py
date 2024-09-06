from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if len(numbers) == 2:
        return (min(numbers), max(numbers))

    closest_1 = float("inf")
    closest_2 = float("inf")

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            current_difference = abs(numbers[i] - numbers[j])
            if current_difference < closest_1:
                closest_1 = current_difference
                closest_1_1 = i
                closest_1_2 = j
            elif current_difference < closest_2:
                closest_2 = current_difference
                closest_2_1 = i
                closest_2_2 = j

    return (numbers[closest_1_1], numbers[closest_1_2]) if closest_1 < closest_2 else (numbers[closest_2_1], numbers[closest_2_2])
