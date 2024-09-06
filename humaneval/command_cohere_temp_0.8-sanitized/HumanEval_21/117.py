from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    
    scaled_numbers = [((x - min_value) / (max_value - min_value)) * 2 for x in numbers]
    
    return scaled_numbers