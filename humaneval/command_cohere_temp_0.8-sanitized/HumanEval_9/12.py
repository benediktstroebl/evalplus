from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_tracker = numbers[0]
    result = [max_tracker]
    
    for cur_num in numbers[1:]:
        if cur_num > max_tracker:
            max_tracker = cur_num
            result.append(max_tracker)
    
    return result