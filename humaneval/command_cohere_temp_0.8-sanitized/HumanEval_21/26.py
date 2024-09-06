from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled = [(value - min_value) / (max_value - min_value) for value in numbers]
    
    return rescaled