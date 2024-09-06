from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(set(numbers))

    for i in range(len(numbers)):
        index_min = i
        index_max = i + 1

        while index_min > 0 and numbers[index_min] - numbers[i] < numbers[i] - numbers[index_max]:
            index_min -= 1

        while index_max < len(numbers) - 1 and numbers[i] - numbers[index_max] < numbers[index_max] - numbers[i]:
            index_max += 1

        if numbers[i] - numbers[index_min] > numbers[index_max] - numbers[i]:
            numbers[index_min], numbers[i] = numbers[i], numbers[index_min]

        if numbers[i] - numbers[index_max] > numbers[index_max] - numbers[i]:
            numbers[index_max], numbers[i] = numbers[i], numbers[index_max]

    return numbers[0], numbers[-1]

