from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_copy = list(numbers)
    nums_copy.sort()
    return nums_copy[0], nums_copy[-1]