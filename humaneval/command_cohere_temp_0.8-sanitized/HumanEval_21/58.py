from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute the range.")
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    scaled_numbers = [((num - min_value) / (max_value - min_value)) * 2 - 1 for num in numbers]
    
    return scaled_numbers