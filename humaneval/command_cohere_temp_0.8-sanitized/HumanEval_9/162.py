from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_maxes[i-1]:
            rolling_maxes[i] = numbers[i]
    return rolling_maxes