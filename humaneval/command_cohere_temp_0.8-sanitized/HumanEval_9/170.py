from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_vals = []
    max_tracker = numbers[0]
    
    for num in numbers[1:]:
        if num > max_tracker:
            max_tracker = num
        rolling_max_vals.append(max_tracker)
    
    return rolling_max_vals