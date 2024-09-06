from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    min_val = min(numbers)
    max_val = max(numbers)
    return [((x - min_val) / (max_val - min_val)) for x in numbers]