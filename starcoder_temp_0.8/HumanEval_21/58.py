from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    numbers_arr = np.array(numbers)
    new_min = 0.0
    new_max = 1.0
    old_min = np.amin(numbers_arr)
    old_max = np.amax(numbers_arr)
    new_range = new_max - new_min
    old_range = old_max - old_min
    scale = new_range / old_range
    shifted = numbers_arr - old_min
    scaled = shifted * scale
    return scaled.tolist()

