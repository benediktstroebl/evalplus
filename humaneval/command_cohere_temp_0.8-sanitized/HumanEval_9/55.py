from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for n in numbers[1:]:
        if n > max_so_far:
            max_so_far = n
        result.append(max_so_far)
    
    return result
numbers = [1, 2, 3, 2, 3, 4, 2]