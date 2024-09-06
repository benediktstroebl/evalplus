from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    #
    # your code here
    #
    if len(numbers) < 2:
        raise ValueError(
            "The number of numbers is less than two, " "therefore there are no closest elements"
        )

    min_diff = float("inf")
    closest_numbers = (None, None)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])

            if diff < min_diff:
                min_diff = diff
                closest_numbers = (numbers[i], numbers[j])

    return closest_numbers

