from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for idx, number in enumerate(numbers[1:]):
        if number > rolling_maxes[idx]:
            rolling_maxes[idx] = number
    return rolling_maxes