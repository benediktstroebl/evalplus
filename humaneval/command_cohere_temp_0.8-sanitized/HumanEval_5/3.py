from typing import List
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result: List[int] = []
    for num in numbers:
        result.append(num)
        result.append(delimiter)
    return result