from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_windows: int) -> List[int]:
    return [max(numbers[i-rolling_windows:i+1]) for i in range(len(numbers)-rolling_windows+1)]