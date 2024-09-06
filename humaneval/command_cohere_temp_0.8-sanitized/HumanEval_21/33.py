from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    return rescaled