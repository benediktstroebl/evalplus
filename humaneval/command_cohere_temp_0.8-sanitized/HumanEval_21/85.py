from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [((x - min(numbers)) / (max(numbers) - min(numbers))) * 2 for x in numbers]
    return [x * (1.0 / 2.0) for x in rescaled]