from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [x / max(numbers) for x in numbers]
    return [x * (1 / min(numbers)) for x in rescaled]