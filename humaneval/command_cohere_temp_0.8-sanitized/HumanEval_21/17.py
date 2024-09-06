from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    if len(numbers) < 2:
        return numbers
    max_num = max(numbers)
    min_num = min(numbers)
    return [((x - min_num) / (max_num - min_num)) for x in numbers]