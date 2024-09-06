from typing import List
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)
numbers = [1, 2, 3]