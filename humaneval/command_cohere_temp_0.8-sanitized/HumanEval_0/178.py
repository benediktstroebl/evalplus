from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) <= threshold for x, y in zip(numbers, numbers[1:]))