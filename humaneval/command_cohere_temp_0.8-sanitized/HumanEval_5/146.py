from typing import List
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result: List[int] = []
    for num in numbers:
        result.append(num)
        if len(result) < len(numbers):
            result.append(delimiter)
    return result