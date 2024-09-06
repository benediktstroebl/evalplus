from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sample_range = (0, 1)  # first and last index to count from
    while sample_range[1] < len(numbers) and sample_range[0] >= 0:
        sample_range = (sample_range[0], sample_range[1] + 1)
        sample = numbers[sample_range[0]:sample_range[1]]
        sample.sort()
    closest = sample[1]

    for index, number in enumerate(sample):
        if index % 2:
            continue
        if number < closest:
            closest = number
        elif number > closest:
            break

    return closest, closest

