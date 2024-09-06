from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) <= 2:
        raise ValueError("There are not enough elements in the list.")

    result = []
    for number in numbers:
        difference = numbers[0] - number
        if number < numbers[0]:
            difference *= -1

        if len(result) == 0:
            result.append(number)
        else:
            if difference <= result[0][1]:
                result.append((number, difference))
                result = sorted(result, key=lambda x: x[1])
    return tuple(sorted(x[0] for x in result))

