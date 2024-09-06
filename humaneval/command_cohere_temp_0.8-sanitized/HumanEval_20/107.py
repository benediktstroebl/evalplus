from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_set = set(numbers)
    if len(nums_set) < 2:
        raise ValueError("Input list must contain at least two unique numbers.")
    
    closest_pair = sorted([(abs(a - b), a, b) for a in nums_set for b in nums_set if a != b])[-1]
    return closest_pair[-1], closest_pair[-2]