from typing import List, Tuple
def rolling_max(numbers: List[int], max_so_far: List[int]=None) -> List[int]:
    if max_so_far is None:
        max_so_far = [numbers[0]] if numbers else []
    if not numbers:
        return max_so_far
    max_so_far[:] = [max(max_so_far[-1], numbers[0])] + max_so_far[:-1]
    return max_so_far