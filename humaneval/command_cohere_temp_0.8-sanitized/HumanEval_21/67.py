from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [x / max(numbers) for x in numbers]