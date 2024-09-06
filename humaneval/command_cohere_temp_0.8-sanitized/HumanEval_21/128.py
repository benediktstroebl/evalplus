from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) for x in numbers]
    
    return rescaled_numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]