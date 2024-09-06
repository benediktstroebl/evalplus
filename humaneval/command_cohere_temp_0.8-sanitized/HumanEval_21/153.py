from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    
    scaled_numbers = [num / max_value for num in numbers]
    return [num * (1 / (max_value - min_value)) for num in scaled_numbers]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]