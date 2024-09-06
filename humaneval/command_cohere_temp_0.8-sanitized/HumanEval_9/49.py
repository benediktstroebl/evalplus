from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_maxes.append(numbers[i])
        else:
            rolling_maxes.append(rolling_maxes[-1])
    return rolling_maxes