from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """

    # get the smallest and largest number from the list
    min_num = min(numbers)
    max_num = max(numbers)
    
    # apply the linear transformation
    return [(num - min_num) / (max_num - min_num) for num in numbers]