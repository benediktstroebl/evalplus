from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_found = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_found.append(num)
            max_so_far = num
    
    return max_found