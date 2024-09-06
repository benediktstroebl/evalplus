from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_windows: int) -> List[int]:
    return [max(list(window)) for window in zip(*[iter(numbers)] * rolling_windows)]