from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for i, x in enumerate(numbers) for j, y in enumerate(numbers[i+1:], i+1) if x < y and abs(x - y) < threshold)