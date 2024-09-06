from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(subsequence)) for subsequence in itertools.accumulate(numbers, rolling_window)]