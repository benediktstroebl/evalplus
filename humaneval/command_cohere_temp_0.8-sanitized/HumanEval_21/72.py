from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [num / nums_range for num in numbers]
    return [0.0 if num == min(numbers) else 1.0 if num == max(numbers) else rescaled[num in rescaled] for num in numbers]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]