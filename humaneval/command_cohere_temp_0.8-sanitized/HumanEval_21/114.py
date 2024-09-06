from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the scale factor
    scale_factor = 1 / (max_value - min_value)
    
    # Rescale each number in the list
    rescaled_numbers = [num * scale_factor for num in numbers]
    
    return rescaled_numbers