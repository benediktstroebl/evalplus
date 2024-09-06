from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers or len(numbers) == 1:
        return numbers
    return [(x-min(numbers))/(max(numbers)-min(numbers)) * 1 for x in numbers]