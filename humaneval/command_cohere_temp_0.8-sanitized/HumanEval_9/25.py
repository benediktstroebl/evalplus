from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_seen = numbers[0]
    result = [max_seen] * len(numbers)
    for i in range(1, len(numbers)):
        max_seen = max(numbers[i], max_seen)
        result[i] = max_seen
    return result