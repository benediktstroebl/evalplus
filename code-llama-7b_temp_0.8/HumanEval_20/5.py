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
        raise ValueError("The list needs to be longer than 1.")

    closest_elements: List[float] = []

    for number in numbers:
        if len(closest_elements) == 0:
            closest_elements.append(number)
        else:
            for index, value in enumerate(closest_elements):
                if abs(number - value) < abs(number - closest_elements[index - 1]):
                    closest_elements.insert(index, number)
                    break
                elif number < value and index == len(closest_elements) - 1:
                    closest_elements.insert(index + 1, number)
                    break
                elif number > value and index == 0:
                    closest_elements.insert(0, number)
                    break
    return closest_elements[0], closest_elements[1]

