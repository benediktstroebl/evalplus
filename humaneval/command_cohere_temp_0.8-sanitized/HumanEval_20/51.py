from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_copy = sorted(numbers)
    diffs = [abs(nums_copy[i] - nums_copy[i-1]) for i in range(1, len(nums_copy))]
    closest_idx = diffs.index(min(diffs))-1
    return nums_copy[closest_idx], nums_copy[closest_idx+1]