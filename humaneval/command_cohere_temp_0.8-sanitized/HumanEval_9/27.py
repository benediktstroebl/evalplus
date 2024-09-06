from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen]
    for n in numbers[1:]:
        if n > max_seen:
            max_seen = n
        result.append(max_seen)
    return result