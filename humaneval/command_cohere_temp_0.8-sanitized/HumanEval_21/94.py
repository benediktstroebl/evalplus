from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the scale factor for the linear transformation
    scale_factor = 1 / (max_value - min_value)
    
    # Rescale each number in the list
    rescaled_numbers = [number * scale_factor for number in numbers]
    
    # Clamp rescaled values between 0 and 1 (optional, based on problem statement)
    # rescaled_numbers = [max(0, min(1, number)) for number in rescaled_numbers]
    
    return rescaled_numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]