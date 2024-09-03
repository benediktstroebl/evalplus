from typing import List
def rescale_to_unit(numbers: List[float]):
    numbers = [x / 100.0 for x in numbers]
    return numbers