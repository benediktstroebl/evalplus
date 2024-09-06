from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [x / min(numbers) for x in numbers]
    return [x * (1 / max(numbers)) for x in rescaled]