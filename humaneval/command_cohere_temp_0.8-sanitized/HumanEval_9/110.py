from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_list = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
            max_list.append(max_so_far)
        
    return max_list