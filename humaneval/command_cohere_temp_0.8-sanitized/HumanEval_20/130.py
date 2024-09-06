from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    return nums_sorted[0], nums_sorted[-1]