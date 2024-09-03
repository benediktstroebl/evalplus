from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]