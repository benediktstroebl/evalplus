from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_return = []
    for i in range(len(numbers)):
        max_found = max(numbers[i], rolling_max_return[-1])
        rolling_max_return.append(max_found)
    return rolling_max_return