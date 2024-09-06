from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_vals = []
    for i in range(len(numbers)):
        max_vals.append(max(numbers[i:i+2]))
    return max_vals