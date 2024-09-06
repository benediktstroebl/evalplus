from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if numbers is None or len(numbers) < 2:
        raise Exception("List must have at least two elements")

    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num

        if num > max_num:
            max_num = num

    if min_num == max_num:
        return (min_num, max_num)

    min_index = numbers.index(min_num)
    max_index = numbers.index(max_num)

    if min_index > max_index:
        return (min_num, max_num)

    return (numbers[min_index + 1], numbers[max_index + 1])
