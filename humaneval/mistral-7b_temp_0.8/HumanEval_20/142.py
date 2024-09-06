from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("The list must have a minimum length of 2.")

    smallest_number = min(numbers)
    largest_number = max(numbers)

    # Get the smallest difference between numbers
    diff_dict = {}
    for number in numbers:
        difference = abs(number - smallest_number)
        if difference not in diff_dict:
            diff_dict[difference] = [number]
        else:
            diff_dict[difference].append(number)

    for difference in diff_dict:
        if len(diff_dict[difference]) > 1:
            break
    else:
        raise ValueError(
            "The numbers must be of different values. They must not all be equal."
        )

    return sorted([smallest_number, largest_number])
