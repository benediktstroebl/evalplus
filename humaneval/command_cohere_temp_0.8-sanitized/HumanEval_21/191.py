from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) * 255 for x in numbers]
    
    # Clip the values between 0 and 255 to handle potential cases where the calculation might yield nonsense values
    return [max(min(rescaled_num, 255.0), 0) for rescaled_num in rescaled_numbers]