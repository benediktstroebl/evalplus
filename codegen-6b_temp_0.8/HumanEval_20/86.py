from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) > 1

    numbers.sort()
    picked_numbers = [numbers.pop(0), numbers.pop(0)]

    for num in numbers:
        if abs(num - picked_numbers[0]) < abs(picked_numbers[1] - picked_numbers[0]):
            picked_numbers[1] = picked_numbers[0]
            picked_numbers[0] = num
        elif abs(num - picked_numbers[1]) < abs(picked_numbers[1] - picked_numbers[0]):
            picked_numbers[1] = num
        else:
            pass

    return picked_numbers

