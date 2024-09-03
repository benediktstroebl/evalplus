from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Rescales the provided list of numbers such that the smallest number becomes 0 and the largest becomes 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled