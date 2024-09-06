from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [x / num for num, x in zip(sorted(numbers), range(len(numbers), 0, -1))]
    return rescaled