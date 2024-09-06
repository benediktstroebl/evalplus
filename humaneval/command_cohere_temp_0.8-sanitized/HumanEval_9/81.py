from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [numbers[0]]
    for idx, number in enumerate(numbers[1:]):
        if number > rolling_maxes[-1]:
            rolling_maxes.append(number)
        elif number == rolling_maxes[-1]:
            rolling_maxes.append(rolling_maxes[-1])
    return rolling_maxes