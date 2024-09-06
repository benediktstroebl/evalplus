from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result: List[int] = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    return result[:-1]