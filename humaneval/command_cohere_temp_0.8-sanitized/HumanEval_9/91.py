from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(subseq)) for subseq in zip(*[iter(numbers)]*rolling_window)]