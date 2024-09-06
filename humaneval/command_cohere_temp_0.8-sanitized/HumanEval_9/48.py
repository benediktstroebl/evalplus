from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_tracker = numbers[0]
    max_list = [max_tracker]
    for num in numbers[1:]:
        if num > max_tracker:
            max_tracker = num
            max_list.append(max_tracker)
        else:
            max_list.append(max_tracker)
    return max_list