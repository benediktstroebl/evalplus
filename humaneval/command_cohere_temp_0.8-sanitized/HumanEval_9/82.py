from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = []
    for i in range(len(numbers)):
        max_so_far = max(numbers[i], rolling_maxes[-1]) if rolling_maxes else numbers[i]
        rolling_maxes.append(max_so_far)
    return rolling_maxes