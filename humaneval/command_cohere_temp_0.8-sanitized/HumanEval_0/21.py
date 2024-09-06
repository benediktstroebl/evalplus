from typing import List
import heapq as hq
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    min_val, max_val = hq.nsmallest(2, numbers), hq.nlargest(2, numbers)
    return min_val[1] - max_val[0] < threshold