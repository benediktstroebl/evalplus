from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_windows: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][:rolling_windows]) for nums in numbers[1:]]