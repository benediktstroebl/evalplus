from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    return numbers[1], numbers[2]