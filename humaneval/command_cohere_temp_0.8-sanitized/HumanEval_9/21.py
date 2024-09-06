from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_list = [max_so_far]
    
    for idx, number in enumerate(numbers[1:]):
        if number > max_so_far:
            max_so_far = number
            max_list.append(max_so_far)
        max_list[idx + 1] = max_so_far
    
    return max_list