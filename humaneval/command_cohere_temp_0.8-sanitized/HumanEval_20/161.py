from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = abs(nums_sorted[-1] - nums_sorted[0])
    return nums_sorted[0], nums_sorted[-1] if diff == abs(nums_sorted[0] - nums_sorted[-1]) else nums_sorted[1], nums_sorted[2]