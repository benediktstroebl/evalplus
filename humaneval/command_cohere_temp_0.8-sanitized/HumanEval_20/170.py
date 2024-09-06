from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_copy = list(numbers)
    len_nums = len(nums_copy)
    
    if len_nums < 2:
        raise ValueError("List of numbers must have at least two elements")
    
    min_distance = float('inf')
    min_distance_idx1, min_distance_idx2 = -1, -1
    
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            distance = abs(nums_copy[i] - nums_copy[j])
            if distance < min_distance:
                min_distance = distance
                min_distance_idx1, min_distance_idx2 = i, j
    
    return nums_copy[min_distance_idx1], nums_copy[min_distance_idx2]