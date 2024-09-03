from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num + delimeter for num in numbers[1:]]
numbers = [1, 2, 3]