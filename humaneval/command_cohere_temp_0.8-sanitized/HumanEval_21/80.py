from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled_numbers = [0 if number == min(numbers) else (number - min(numbers)) / (max(numbers) - min(numbers)) for number in numbers]
    return rescaled_numbers